# Copyright (c) 2013, Web Notes Technologies Pvt. Ltd. and Contributors
# MIT License. See license.txt

from __future__ import unicode_literals
import datetime

from frappe import _
import frappe
import frappe.database
import frappe.utils
import frappe.utils.user
from frappe import conf
from frappe.sessions import Session, clear_sessions, delete_session
from frappe.modules.patch_handler import check_session_stopped

from urllib import quote

class HTTPRequest:
	def __init__(self):
		# Get Environment variables
		self.domain = frappe.request.host
		if self.domain and self.domain.startswith('www.'):
			self.domain = self.domain[4:]

		frappe.local.request_ip = frappe.get_request_header('REMOTE_ADDR') \
				or frappe.get_request_header('X-Forwarded-For') or '127.0.0.1'
		# language
		self.set_lang(frappe.get_request_header('HTTP_ACCEPT_LANGUAGE'))

		# load cookies
		frappe.local.cookie_manager = CookieManager()

		# override request method. All request to be of type POST, but if _type == "POST" then commit
		if frappe.form_dict.get("_type"):
			frappe.local.request_method = frappe.form_dict.get("_type")
			del frappe.form_dict["_type"]

		# set db
		self.connect()

		# login
		frappe.local.login_manager = LoginManager()

		# write out latest cookies
		frappe.local.cookie_manager.init_cookies()

		# check status
		check_session_stopped()

		# load user
		self.setup_user()

		# run login triggers
		if frappe.form_dict.get('cmd')=='login':
			frappe.local.login_manager.run_trigger('on_session_creation')

	def set_lang(self, lang):
		from frappe.translate import guess_language_from_http_header
		frappe.local.lang = guess_language_from_http_header(lang)

	def setup_user(self):
		frappe.local.user = frappe.utils.user.User()

	def get_db_name(self):
		"""get database name from conf"""
		return conf.db_name

	def connect(self, ac_name = None):
		"""connect to db, from ac_name or db_name"""
		frappe.local.db = frappe.database.Database(user = self.get_db_name(), \
			password = getattr(conf,'db_password', ''))

class LoginManager:
	def __init__(self):
		self.user = None
		if frappe.local.form_dict.get('cmd')=='login' or frappe.local.request.path=="/api/method/login":
			self.login()
		else:
			self.make_session(resume=True)

	def login(self):
		# clear cache
		frappe.clear_cache(user = frappe.form_dict.get('usr'))
		self.authenticate()
		self.post_login()

	def post_login(self):
		self.run_trigger('on_login')
		self.validate_ip_address()
		self.validate_hour()
		self.make_session()
		self.set_user_info()

	def set_user_info(self):
		# set sid again
		frappe.local.cookie_manager.init_cookies()

		info = frappe.db.get_value("User", self.user,
			["user_type", "first_name", "last_name", "user_image"], as_dict=1)
		if info.user_type=="Website User":
			frappe.local.cookie_manager.set_cookie("system_user", "no")
			frappe.local.response["message"] = "No App"
		else:
			frappe.local.cookie_manager.set_cookie("system_user", "yes")
			frappe.local.response['message'] = 'Logged In'

		full_name = " ".join(filter(None, [info.first_name, info.last_name]))
		frappe.response["full_name"] = full_name
		frappe.local.cookie_manager.set_cookie("full_name", full_name)
		frappe.local.cookie_manager.set_cookie("user_id", self.user)
		frappe.local.cookie_manager.set_cookie("user_image", info.user_image or "")

	def make_session(self, resume=False):
		# start session
		frappe.local.session_obj = Session(user=self.user, resume=resume)

		# reset user if changed to Guest
		self.user = frappe.local.session_obj.user
		frappe.local.session = frappe.local.session_obj.data

	def authenticate(self, user=None, pwd=None):
		if not (user and pwd):
			user, pwd = frappe.form_dict.get('usr'), frappe.form_dict.get('pwd')
		if not (user and pwd):
			self.fail('Incomplete login details')

		self.check_if_enabled(user)
		self.user = self.check_password(user, pwd)

	def check_if_enabled(self, user):
		"""raise exception if user not enabled"""
		from frappe.utils import cint
		if user=='Administrator' or user=='administrator' : return
		if not cint(frappe.db.get_value('User', user, 'enabled')):
			self.fail('User disabled or missing')
		user = frappe.db.sql("""select `name` from tabUser where validity_start_date <= CURDATE() and validity_end_date >= CURDATE() and name=%s """, (user))
		if user:
			pass
		else:	
			self.fail('vaildity end please contact administrator')
	def check_password(self, user, pwd):
		"""check password"""
		user = frappe.db.sql("""select `user` from __Auth where `user`=%s and `password`=password(%s)""", (user, pwd))
		if not user:
			self.fail('Incorrect password ')
		else:
			return user[0][0] # in correct case

	def fail(self, message):
		frappe.local.response['message'] = message
		raise frappe.AuthenticationError

	def run_trigger(self, event='on_login'):
		for method in frappe.get_hooks().get(event, []):
			frappe.call(frappe.get_attr(method), login_manager=self)

	def validate_ip_address(self):
		"""check if IP Address is valid"""
		ip_list = frappe.db.get_value('User', self.user, 'restrict_ip', ignore=True)
		if not ip_list:
			return

		ip_list = ip_list.replace(",", "\n").split('\n')
		ip_list = [i.strip() for i in ip_list]

		for ip in ip_list:
			if frappe.local.request_ip.startswith(ip):
				return

		frappe.throw(_("Not allowed from this IP Address"), frappe.AuthenticationError)

	def validate_hour(self):
		"""check if user is logging in during restricted hours"""
		login_before = int(frappe.db.get_value('User', self.user, 'login_before', ignore=True) or 0)
		login_after = int(frappe.db.get_value('User', self.user, 'login_after', ignore=True) or 0)

		if not (login_before or login_after):
			return

		from frappe.utils import now_datetime
		current_hour = int(now_datetime().strftime('%H'))

		if login_before and current_hour > login_before:
			frappe.throw(_("Login not allowed at this time"), frappe.AuthenticationError)

		if login_after and current_hour < login_after:
			frappe.throw(_("Login not allowed at this time"), frappe.AuthenticationError)

	def login_as_guest(self):
		"""login as guest"""
		self.user = 'Guest'
		self.post_login()

	def logout(self, arg='', user=None):
		if not user: user = frappe.session.user
		self.run_trigger('on_logout')

		if user == frappe.session.user:
			delete_session(frappe.session.sid)
			self.clear_cookies()
		else:
			clear_sessions(user)

	def clear_cookies(self):
		clear_cookies()

class CookieManager:
	def __init__(self):
		self.cookies = {}
		self.to_delete = []

	def init_cookies(self):
		if not frappe.local.session.get('sid'): return

		# sid expires in 3 days
		expires = datetime.datetime.now() + datetime.timedelta(days=3)
		if frappe.session.sid:
			self.cookies["sid"] = {"value": frappe.session.sid, "expires": expires}
		if frappe.session.session_country:
			self.cookies["country"] = {"value": frappe.session.get("session_country")}

	def set_cookie(self, key, value, expires=None):
		self.cookies[key] = {"value": value, "expires": expires}

	def delete_cookie(self, to_delete):
		if not isinstance(to_delete, (list, tuple)):
			to_delete = [to_delete]

		self.to_delete.extend(to_delete)

	def flush_cookies(self, response):
		for key, opts in self.cookies.items():
			response.set_cookie(key, quote((opts.get("value") or "").encode('utf-8')),
				expires=opts.get("expires"))

		# expires yesterday!
		expires = datetime.datetime.now() + datetime.timedelta(days=-1)
		for key in set(self.to_delete):
			response.set_cookie(key, "", expires=expires)

def _update_password(user, password):
	frappe.db.sql("""insert into __Auth (user, `password`)
		values (%s, password(%s))
		on duplicate key update `password`=password(%s)""", (user,
		password, password))

@frappe.whitelist()
def get_logged_user():
	return frappe.session.user

def clear_cookies():
	if hasattr(frappe.local, "session"):
		frappe.session.sid = ""
	frappe.local.cookie_manager.delete_cookie(["full_name", "user_id", "sid", "user_image", "system_user"])
