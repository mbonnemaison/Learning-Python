"""
Roman to Integer (Leetcode problem #13)
Roman numerals are represented by seven different symbols:
I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

For example, 2 is written as II in Roman numeral, just two one's added together.
12 is written as XII, which is simply X + II.
The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right.
However, the numeral for four is not IIII. Instead, the number four is written
as IV. Because the one is before the five we subtract it making four.
The same principle applies to the number nine, which is written as IX.
There are six instances where subtraction is used:

    I can be placed before V (5) and X (10) to make 4 and 9.
    X can be placed before L (50) and C (100) to make 40 and 90.
    C can be placed before D (500) and M (1000) to make 400 and 900.

Given a roman numeral, convert it to an integer.

Example 1:
Input: s = "III"
Output: 3

Example 2:
Input: s = "IV"
Output: 4

Example 3:
Input: s = "IX"
Output: 9

Example 4:
Input: s = "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.

Example 5:
Input: s = "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.

Constraints:
    1 <= s.length <= 15
    s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
    It is guaranteed that s is a valid roman numeral in the range [1, 3999].

class Solution:
    def romanToInt(self, s: str) -> int:

"""
class Solution:
    def romanToInt(self, s):
        n = 0
        numeral = 0
        while n < len(s):
            if s[n] == "I":
                if n+1 == len(s):
                    numeral += 1
                    n += 1
                elif s[n+1] == "V":
                    numeral += 4
                    n += 2
                elif s[n+1] == "X":
                    numeral += 9
                    n += 2
                else:
                    numeral += 1
                    n += 1
            elif s[n] == "V":
                numeral += 5
                n += 1
            elif s[n] == "X":
                if n+1 == len(s):
                    numeral += 10
                    n += 1
                elif s[n+1] == "L":
                    numeral += 40
                    n += 2
                elif s[n+1] == "C":
                    numeral += 90
                    n += 2
                else:
                    numeral += 10
                    n += 1
            elif s[n] == "L":
                numeral += 50
                n += 1
            elif s[n] == "C":
                if n+1 == len(s):
                    numeral += 100
                    n += 1
                elif s[n+1] == "D":
                    numeral += 400
                    n += 2
                elif s[n+1] == "M":
                    numeral += 900
                    n += 2
                else:
                    numeral += 100
                    n += 1
            elif s[n] == "D":
                numeral += 500
                n += 1
            elif s[n] == "M":
                numeral += 1000
                n += 1
        return numeral

k = Solution()
print(k.romanToInt(s="MMMCC"))
