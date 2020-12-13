"""Test test file
"""
from test import *

__author__ = "help@castellanidavide.it"
__version__ = "1.0 2020-12-13"

def test():
	"""Tests the test function in the test class
	Write here all test you want to do.
	REMEMBER to test your programm you can't use __init__ function
	"""
	assert test.test() == "test", "test failed"
	#assert test.<function>(<values>) == <the result(s) you would like to have>, "<the fail message>"
	
if __name__ == "__main__":
	test()
