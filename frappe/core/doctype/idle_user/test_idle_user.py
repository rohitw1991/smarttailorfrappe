# Copyright (c) 2013, Web Notes Technologies Pvt. Ltd. and Contributors
# See license.txt

import frappe
import unittest

test_records = frappe.get_test_records('Idle User')

class TestIdleUser(unittest.TestCase):
	pass
