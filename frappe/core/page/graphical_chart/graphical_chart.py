from __future__ import unicode_literals
import frappe
from frappe import _
import frappe.defaults
import frappe.permissions
from frappe.core.doctype.user.user import get_system_users
from frappe.utils.csvutils import UnicodeWriter, read_csv_content_from_uploaded_file
from frappe.defaults import clear_default
import datetime

def formated_date(date_str):
	return  datetime.datetime.strptime(date_str , '%d-%m-%Y').strftime('%Y-%m-%d')
	 
@frappe.whitelist()
def get_data(from_date=None,to_date=None,currency=None):
	frappe.errprint(currency)
	data_dict = {'cols':'name ,net_total', 'tab':'`tabSales Order`', 'cond_col': 'delivery_date','cncy':'currency'}
	make_cond(data_dict, from_date, to_date,currency)				
	return{
		"sales_order_total": make_query(data_dict)
	}
	
@frappe.whitelist()
def get_jv_data(from_date=None,to_date=None):
	data_dict = {'cols':'name,total_credit', 'tab':'`tabJournal Voucher`', 'cond_col': 'posting_date'}
	make_cond(data_dict, from_date, to_date)				
	return{
		"order_total": make_query(data_dict)
	}
	

def make_cond(data_dict, from_date=None,to_date=None,currency=None):
	if from_date and to_date:
		data_dict['cond'] = """ where %(cond_col)s between '%(from_date)s' and '%(to_date)s and %(cncy)s= '%(currency)s'
			"""%{'cond_col': data_dict.get('cond_col'), 'from_date': formated_date(from_date),
					'to_date': formated_date(to_date),'currency':currency, 'cncy':data_dict.get('cncy')}
	else:
		data_dict['cond'] = ' '

def make_query(data_dict):
	return frappe.db.sql("select %(cols)s from %(tab)s %(cond)s"%data_dict)

@frappe.whitelist()
def get_activities():
	dbname=frappe.db.sql("""select site_name from `tabSubAdmin Info` where active=1""",as_dict=1)
	lst=[]
	qry_srt='select subject,site_name from('
	for key in dbname:
		temp =key['site_name']
		qry="SELECT subject,creation,'%s' as site_name FROM "%(temp)
		if temp :
			qry+=temp+'.tabFeed'
			lst.append(qry)
	fin_qry=' UNION '.join(lst)
	qry=qry_srt+fin_qry+" where doc_name='Administrator')foo ORDER BY creation DESC limit 5"
	act_details=frappe.db.sql(fin_qry,as_dict=1)
	return act_details


@frappe.whitelist()
def get_data_newsale(from_date=None,to_date=None):
	if from_date and to_date:
		str1="select date_format(creation,'%M') as month,count(*) as lead from `tabLead` where date(creation) between '"+formated_date(from_date)+"' and '"+formated_date(to_date)+"' order by month"
		sales_details=frappe.db.sql(str1,debug=1)
		return{
		"order_total": sales_details
	    }
	else:
		str1="select date_format(creation,'%M') as month,count(*) as lead from `tabLead` order by month"
		sales_details=frappe.db.sql(str1,debug=1)
		return{
		"order_total": sales_details
	    }

@frappe.whitelist()
def get_prospect(from_date=None,to_date=None):
	frappe.errprint("in the pro py")
	frappe.errprint(from_date)
	frappe.errprint(to_date)

	if from_date and to_date:
		str2="select name,sum(target_amount*percentage_allocation/100)as target_amount from (SELECT sp.name,bd.fiscal_year,bdd.month,bdd.percentage_allocation,(select sum(td.target_amount) from `tabTarget Detail` td where td.parent=sp.name and td.fiscal_year=bd.fiscal_year) as target_amount,(case when bdd.month in('January','February','March') then SUBSTRING_INDEX(SUBSTRING_INDEX(bd.fiscal_year, '-', 1), ' ', -1)  else SUBSTRING_INDEX(SUBSTRING_INDEX(bd.fiscal_year, '-', -1), ' ', -1) end) as year FROM `tabSales Person` sp,`tabBudget Distribution` bd,`tabBudget Distribution Detail` bdd where sp.distribution_id=bd.name and bdd.parent=bd.name )foo where date_format(str_to_date(concat('01-',month,'-',year),'%d-%M-%Y'),'%y-%m') between date_format(date('"+formated_date(from_date)+"'),'%y-%m') and date_format(date('"+formated_date(to_date)+"'),'%y-%m') group by name"
		frappe.errprint(str2)
		prospect_details=frappe.db.sql(str2,debug=1)
		frappe.errprint(prospect_details)
		return{
		"order_total": prospect_details
	    }
	# else:
	# 	str1="select date_format(creation,'%M') as month,count(*) as lead from `tabLead` order by month"
	# 	sales_details=frappe.db.sql(str1,debug=1)
	# 	return{
	# 	"order_total": sales_details
	#     }	    


@frappe.whitelist()
def get_subscription(from_date=None,to_date=None):
	frappe.errprint("in the get_subscription py")
	#frappe.errprint(from_date)
	#frappe.errprint(to_date)
	#frappe.errprint("calling ")
	if from_date and to_date:
		str2="select name,EXTRACT(month FROM expiry_date) as expiry_date  from `tabSite Master` where expiry_date between '2013-12-25' and '2015-12-25'"
		#frappe.errprint(str2)
		subscription_details=frappe.db.sql(str2,as_list=1)
		frappe.errprint(subscription_details)
		return{
		"order_total": subscription_details
	    }
	else:
		str2="select name,EXTRACT(month FROM expiry_date) as expiry_date  from `tabSite Master` where expiry_date is not null"
		#frappe.errprint(str2)
		subscription_details=frappe.db.sql(str2,as_list=1)
		frappe.errprint(subscription_details)
		return{
		"order_total": subscription_details
	    }

		    

