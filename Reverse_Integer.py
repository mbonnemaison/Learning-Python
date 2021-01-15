"""
Reverse Integer (Leetcode problem #7)
Given a signed 32-bit integer x, return x with its digits reversed. If
reversing x causes the value to go outside the signed 32-bit integer range
[-2^31, 2^31 - 1], then return 0.
Assume the environment does not allow you to store 64-bit integers
(signed or unsigned).

Example 1:
Input: x = 123
Output: 321

Example 2:
Input: x = -123
Output: -321

Example 3:
Input: x = 120
Output: 21

Example 4:
Input: x = 0
Output: 0

Constraints:
    -2^31 <= x <= 2^31 - 1

class Solution:
    def reverse(self, x: int) -> int:

"""
class Solution:
    def reverse(self, x):
        y = str(abs(x))
        n = len(y) - 1
        a = None
        while n >= 0:
            if a is None:
                a = y[n]
                n = n - 1
            else:
                a = a + y[n]
                n = n - 1
        if x < 0:
            z = int(a)*-1
        else:
            z = int(a)
        if -2147483648 <= z <= 2147483647:
            return z
        else:
            return 0

#Examples to test the code:
s = Solution()
print(s.reverse(x=23))
