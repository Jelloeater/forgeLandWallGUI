from unittest import TestCase

__author__ = 'Jesse'

import model
class TestMessage(TestCase):
	def test_getMessagesFromServer(self):
		""" Make sure we get a proper index (will fail on an empty table)"""
		x = model.message.getMessagesFromServer(1)
		testVar = x[0]['index']
		self.assertEqual(True, str.isdigit(str(testVar)), "No Number Found in [0]['index']")