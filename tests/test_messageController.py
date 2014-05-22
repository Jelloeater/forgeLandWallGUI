from unittest import TestCase
from controler import messageController
__author__ = 'Jesse'


class TestMessageController(TestCase):
	def test_refreshMessageList(self):
		""" Make sure we get a proper index (will fail on an empty table)"""
		x = messageController.refreshMessageList(1)
		testVar = x[0]['index']
		self.assertEqual(True, str.isdigit(str(testVar)), "No Number Found in [0]['index']")