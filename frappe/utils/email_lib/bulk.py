# Copyright (c) 2013, Web Notes Technologies Pvt. Ltd. and Contributors
# MIT License. See license.txt

from __future__ import unicode_literals
import frappe
import HTMLParser
import urllib
from frappe import msgprint, throw, _
from frappe.utils.email_lib.smtp import SMTPServer
from frappe.utils.email_lib.email_body import get_email, get_formatted_html
from frappe.utils.email_lib.html2text import html2text
from frappe.utils import cint, get_url, nowdate

class BulkLimitCrossedError(frappe.ValidationError): pass

def send(recipients=None, sender=None, doctype='User', email_field='email',
		subject='[No Subject]', message='[No Content]', ref_doctype=None,
		ref_docname=None, add_unsubscribe_link=True, attachments=None):

	def is_unsubscribed(rdata):
		if not rdata:
			return 1
		return cint(rdata.unsubscribed)

	def check_bulk_limit(new_mails):
		this_month = frappe.db.sql("""select count(*) from `tabBulk Email` where
			month(creation)=month(%s)""" % nowdate())[0][0]

		# No limit for own email settings
		smtp_server = SMTPServer()
		if smtp_server.email_settings and cint(smtp_server.email_settings.enabled):
			monthly_bulk_mail_limit = 999999
		else:
			monthly_bulk_mail_limit = frappe.conf.get('monthly_bulk_mail_limit') or 500

		if ( this_month + len(recipients) ) > monthly_bulk_mail_limit:
			throw(_("Bulk email limit {0} crossed").format(monthly_bulk_mail_limit),
				BulkLimitCrossedError)

	def update_message(formatted, doc, add_unsubscribe_link):
		updated = formatted
		if add_unsubscribe_link:
			unsubscribe_link = """<div style="padding: 7px; border-top: 1px solid #aaa;
				margin-top: 17px;">
				<small><a href="%s/?%s">
				Unsubscribe</a> from this list.</small></div>""" % (get_url(),
				urllib.urlencode({
					"cmd": "frappe.utils.email_lib.bulk.unsubscribe",
					"email": doc.get(email_field),
					"type": doctype,
					"email_field": email_field
				}))

			updated = updated.replace("<!--unsubscribe link here-->", unsubscribe_link)

		return updated

	if not recipients: recipients = []
	if not sender or sender == "Administrator":
		sender = frappe.db.get_value('Outgoing Email Settings', None, 'auto_email_id')
	check_bulk_limit(len(recipients))

	formatted = get_formatted_html(subject, message)

	for r in filter(None, list(set(recipients))):
		rdata = frappe.db.sql("""select * from `tab%s` where %s=%s""" % (doctype,
			email_field, '%s'), (r,), as_dict=1)

		doc = rdata and rdata[0] or {}

		if (not add_unsubscribe_link) or (not is_unsubscribed(doc)):
			# add to queue
			updated = update_message(formatted, doc, add_unsubscribe_link)
			try:
				text_content = html2text(updated)
			except HTMLParser.HTMLParseError:
				text_content = "[See html attachment]"

			add(r, sender, subject, updated, text_content, ref_doctype, ref_docname, attachments)

def add(email, sender, subject, formatted, text_content=None,
	ref_doctype=None, ref_docname=None, attachments=None):
	"""add to bulk mail queue"""
	e = frappe.new_doc('Bulk Email')
	e.sender = sender
	e.recipient = email
	try:
		e.message = get_email(email, sender=e.sender, formatted=formatted, subject=subject,
			text_content=text_content, attachments=attachments).as_string()
	except frappe.InvalidEmailAddressError:
		# bad email id - don't add to queue
		return

	e.status = 'Not Sent'
	e.ref_doctype = ref_doctype
	e.ref_docname = ref_docname
	e.save(ignore_permissions=True)

@frappe.whitelist(allow_guest=True)
def unsubscribe():
	doctype = frappe.form_dict.get('type')
	field = frappe.form_dict.get('email_field')
	email = frappe.form_dict.get('email')

	frappe.db.sql("""update `tab%s` set unsubscribed=1
		where `%s`=%s""" % (doctype, field, '%s'), (email,))

	if not frappe.form_dict.get("from_test"):
		frappe.db.commit()

	frappe.local.message_title = "Unsubscribe"
	frappe.local.message = "<h3>Unsubscribed</h3><p>%s has been successfully unsubscribed.</p>" % email

	frappe.response['type'] = 'page'
	frappe.response['page_name'] = 'message.html'

def flush(from_test=False):
	"""flush email queue, every time: called from scheduler"""
	smtpserver = SMTPServer()

	auto_commit = not from_test

	if frappe.flags.mute_emails or frappe.conf.get("mute_emails") or False:
		msgprint(_("Emails are muted"))
		from_test = True

	for i in xrange(500):
		email = frappe.db.sql("""select * from `tabBulk Email` where
			status='Not Sent' limit 1 for update""", as_dict=1)
		if email:
			email = email[0]
		else:
			break

		frappe.db.sql("""update `tabBulk Email` set status='Sending' where name=%s""",
			(email["name"],), auto_commit=auto_commit)
		try:
			if not from_test:
				smtpserver.sess.sendmail(email["sender"], email["recipient"], email["message"])

			frappe.db.sql("""update `tabBulk Email` set status='Sent' where name=%s""",
				(email["name"],), auto_commit=auto_commit)

		except Exception, e:
			frappe.db.sql("""update `tabBulk Email` set status='Error', error=%s
				where name=%s""", (unicode(e), email["name"]), auto_commit=auto_commit)

def clear_outbox():
	"""remove mails older than 30 days in Outbox"""
	frappe.db.sql("""delete from `tabBulk Email` where
		datediff(now(), creation) > 30""")


def multitenanct(from_test=False):
   res=frappe.db.sql("""select name from `tabSite Master` where flag=0 limit 1 """)
   if res:
	sites=''
	sites = frappe.db.sql("""select sites from  `tabUser` where name='administrator'""")
	print sites
	auto_commit = not from_test
	ste=res[0][0]
	from frappe.utils import cstr  
	import os
	import sys
	import subprocess
	import getpass
	import logging
	import json
	from distutils.spawn import find_executable
	cwd= '/home/gangadhar/workspace/smarttailor/frappe-bench/'
        cmd='bench new-site '+ste
	 
	sites=cstr(sites[0][0])+' '+ste
	print sites
	frappe.db.sql("update `tabUser` set sites= %s where name='administrator'",sites)
        try:
		subprocess.check_call(cmd, cwd=cwd, shell=True)
	except subprocess.CalledProcessError, e:
		print "Error:", e.output
		raise
        cmd='bench frappe --install_app erpnext '+ste              
        try:
		subprocess.check_call(cmd, cwd=cwd, shell=True)
	except subprocess.CalledProcessError, e:
		print "Error:", e.output
		raise
        cmd='bench frappe --install_app shopping_cart '+ste             
        try:
		subprocess.check_call(cmd, cwd=cwd, shell=True)
	except subprocess.CalledProcessError, e:
		print "Error:", e.output
		raise
        nginx="""
		upstream frappe {
    		server 127.0.0.1:8000 fail_timeout=0;
		}
		server {
			listen 80 ;
			client_max_body_size 4G;
			server_name %s;
			keepalive_timeout 5;
			sendfile on;
			root /home/gangadhar/workspace/smarttailor/frappe-bench/sites;
			location /private/ {
				internal;
				try_files /$uri =424;
			}
			location /assets {
				try_files $uri =404;
			}

			location / {
				try_files /test/public/$uri @magic;
			}

			location @magic {
				proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
				proxy_set_header Host $host;
				proxy_set_header X-Use-X-Accel-Redirect True;
				proxy_read_timeout 120;
				proxy_redirect off;
				proxy_pass  http://frappe;
			}
		}"""%(sites)
	with open("/home/gangadhar/workspace/smarttailor/frappe-bench/config/nginx.conf","w") as conf_file:
			conf_file.write(nginx)
        cwd='/home/'
        cmd='echo indictrans | sudo service nginx reload'
        try:
		subprocess.check_call(cmd, cwd=cwd, shell=True)
	except subprocess.CalledProcessError, e:
		print "Error:", e.output
		raise
	host="""
		127.0.0.1       localhost
		127.0.1.1       gangadhar-OptiPlex-360
		127.0.0.1       %s


		# The following lines are desirable for IPv6 capable hosts
		::1     ip6-localhost ip6-loopback
		fe00::0 ip6-localnet
		ff00::0 ip6-mcastprefix
		ff02::1 ip6-allnodes
		ff02::2 ip6-allrouters
       """%(sites)
	with open("/home/gangadhar/workspace/smarttailor/frappe-bench/config/hosts","w") as hosts_file:
			hosts_file.write(host)
        os.system('echo indictrans | sudo -S cp /home/gangadhar/workspace/smarttailor/frappe-bench/config/hosts /etc/hosts')
	qry="update `tabSite Master` set flag=1 where name='"+cstr(res[0][0])+"'"
	frappe.db.sql(qry, auto_commit=auto_commit)
        
