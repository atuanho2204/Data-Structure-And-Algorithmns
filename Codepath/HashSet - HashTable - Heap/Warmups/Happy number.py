'''
Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process:
Starting with any positive integer, replace the number by the sum of
the squares of its digits, and repeat the process until the number equals 1
(where it will stay), or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy numbers.

Example:

Input: 19
Output: true
Explanation:
1^2 + 9^2 = 82
8^2 + 2^2 = 68
6^2 + 8^2 = 100
1^2 + 0^2 + 0^2 = 1
'''

class Solution:
	def isHappy(self, n):
		"""
		:type n: int
		:rtype: bool
		"""
		if n == 1:
			return True

		seen = set()
		while n not in seen:
			seen.add(n)
			n = self.calculate(n)

		if n == 1:
			return True
		else:
			return False

	# Helper function to break down the calculator
	def calculate(self, number):
		output = 0

		while number:
			output += (number%10)**2
			number = number // 10

		return output