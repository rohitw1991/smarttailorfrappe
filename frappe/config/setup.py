from frappe import _
from frappe.widgets.moduleview import add_setup_section

def get_data():
	data = [
		{
			"label": _("Users and Permissions"),
			"icon": "icon-group",
			"items": [
				{
					"type": "doctype",
					"name": "User",
					"description": _("System and Website Users")
				},
				{
					"type": "doctype",
					"name": "Role",
					"description": _("User Roles")
				},
				{
					"type": "page",
					"name": "permission-manager",
					"label": "Role Permissions Manager",
					"icon": "icon-lock",
					"description": _("Set Permissions on Document Types and Roles")
				},
				{
					"type": "page",
					"name": "user-permissions",
					"label": _("User Permissions Manager"),
					"icon": "icon-shield",
					"description": _("Set Permissions per User")
				},
				{
					"type": "report",
					"is_query_report": True,
					"doctype": "User",
					"icon": "icon-eye-open",
					"name": "Permitted Documents For User",
					"description": _("Check which Documents are readable by a User")
				},
				{
					"type": "report",
					"is_query_report": True,
					"doctype": "User",
					"icon": "icon-eye-open",
					"name": "Idle Users",
					"description": _("Check which User are not logged in from specified time ")
				},
				{
					"type": "report",
					"is_query_report": True,
					"doctype": "User",
					"icon": "icon-eye-open",
					"name": "Subscribers Activity",
					"description": _("Check Subscribers Activity ")
				},
				{
					"type": "report",
					"is_query_report": True,
					"doctype": "User",
					"icon": "icon-eye-open",
					"name": "SubAdmin Details",
					"description": _("check SubAdmins Username and Password Details")
				}
			]
		},
		{
			"label": _("Settings"),
			"icon": "icon-wrench",
			"items": [
				{
					"type": "doctype",
					"name": "System Settings",
					"label": _("System Settings"),
					"description": _("Language, Date and Time settings"),
					"hide_count": True
				},
				{
					"type": "page",
					"name": "modules_setup",
					"label": _("Show / Hide Modules"),
					"icon": "icon-upload",
					"description": _("Show or hide modules globally.")
				},
				{
					"type": "doctype",
					"name": "Naming Series",
					"description": _("Set numbering series for transactions."),
					"hide_count": True
				},
			]
		},
		{
			"label": _("Data"),
			"icon": "icon-th",
			"items": [
				{
					"type": "page",
					"name": "data-import-tool",
					"label": _("Import / Export Data"),
					"icon": "icon-upload",
					"description": _("Import / Export Data from .csv files.")
				},
				{
					"type": "doctype",
					"name": "Rename Tool",
					"description": _("Rename many items by uploading a .csv file."),
					"hide_count": True
				},
				{
					"type": "doctype",
					"name": "File Data",
					"description": _("Manage uploaded files.")
				}
			]
		},
		{
			"label": _("Workflow"),
			"icon": "icon-random",
			"items": [
				{
					"type": "doctype",
					"name": "Workflow",
					"description": _("Define workflows for forms.")
				},
				{
					"type": "doctype",
					"name": "Workflow State",
					"description": _("States for workflow (e.g. Draft, Approved, Cancelled).")
				},
				{
					"type": "doctype",
					"name": "Workflow Action",
					"description": _("Actions for workflow (e.g. Approve, Cancel).")
				},
			]
		},
		{
			"label": _("Email"),
			"icon": "icon-envelope",
			"items": [
				{
					"type": "doctype",
					"name": "Outgoing Email Settings",
					"description": _("Set outgoing mail server.")
				},
				{
					"type": "doctype",
					"name": "Email Alert",
					"description": _("Setup Email Alert based on various criteria.")
				},
				{
					"type": "doctype",
					"name": "Standard Reply",
					"description": _("Standard replies to common queries.")
				},
			]
		},
		{
			"label": _("Printing and Branding"),
			"icon": "icon-print",
			"items": [
				{
					"type": "doctype",
					"name": "Print Settings",
					"description": _("Set default format, page size, print style etc.")
				},
				{
					"type": "doctype",
					"name": "Print Format",
					"description": _("Customized HTML Templates for printing transctions.")
				},
			]
		},
		{
			"label": _("Customize"),
			"icon": "icon-glass",
			"items": [
				{
					"type": "doctype",
					"name": "Customize Form",
					"description": _("Change field properties (hide, readonly, permission etc.)"),
					"hide_count": True
				},
				{
					"type": "doctype",
					"name": "Custom Field",
					"description": _("Add fields to forms.")
				},
				{
					"type": "doctype",
					"name": "Custom Script",
					"description": _("Add custom javascript to forms.")
				}
			]
		},
		{
			"label": _("System"),
			"icon": "icon-cog",
			"items": [
				{
					"type": "page",
					"name": "applications",
					"label": _("Application Installer"),
					"description": _("Install Applications."),
					"icon": "icon-download"
				},
				{
					"type": "doctype",
					"name": "Backup Manager",
					"label": _("Download Backup"),
					"onclick": "frappe.ui.toolbar.download_backup",
					"icon": "icon-download-alt",
					"description": _("Send download link of a recent backup to System Managers"),
					"hide_count": True
				},
				{
					"type": "doctype",
					"name": "Backup Manager",
					"description": _("Manage cloud backups on Dropbox"),
					"hide_count": True
				},
				{
					"type": "doctype",
					"name": "Scheduler Log",
					"description": _("Log of error on automated events (scheduler).")
				},
			]
		}
	]
	add_setup_section(data, "frappe", "website", _("Website"), "icon-globe")
	return data
