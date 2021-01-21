"""
Palindrome number (Leetcode problem #9)
Given an integer x, return true if x is palindrome integer.
An integer is a palindrome when it reads the same backward as forward.
For example, 121 is palindrome while 123 is not.

Example 1:
Input: x = 121
Output: true

Example 2:
Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left,
it becomes 121-. Therefore it is not a palindrome.

Example 3:
Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

Example 4:
Input: x = -101
Output: false

Constraints:
    -2^31 <= x <= 2^31 - 1

class Solution:
  def isPalindrome(self, x: int) -> bool:

"""
class Solution:
    def isPalindrome(self, x):
        #print("x=", x, "; y=", y)
        return str(x) == str(x)[::-1]

s = Solution()
print(s.isPalindrome(x=10))

#===============================================================================
"""
Original sbmitted code:
class Solution:
    def isPalindrome(self, x):
        x_str = str(x)
        y = x_str[::-1]
        #print("x=", x, "; y=", y)
        if x_str == y:
            return True
        else:
            return False

s = Solution()
print(s.isPalindrome(x=10))

#===============================================================================
#The following 2 if/else expressions are equivalent to the if/else statement above:
#return True if x_str == y else False
#return x_str == y
"""
