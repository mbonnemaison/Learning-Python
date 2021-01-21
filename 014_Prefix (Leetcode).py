"""
Longest common prefix (Leetcode problem #014)

Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".

Example 1:
Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:
Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

Constraints:
    0 <= strs.length <= 200
    0 <= strs[i].length <= 200
    strs[i] consists of only lower-case English letters.

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

"""
class Solution:
    def longestCommonPrefix(self, strs):
        #Figure out the shortest word in the list:
        #x is the number of letters found in the shortest word in the list.
        output = ""
        if strs == []:
            return output
        x = None
        for i in strs:
            if x is None:
                x = len(i)
            if len(i) < x:
                x = len(i)
        n = 0 #to go through every letter in the words
        m = 0 #to continue loop until we reach the end of shortest word
        while m < x:
            k = 0
            for j in strs:
                if strs[0][n] == j[n]:
                    k += 1
                    if k == len(strs):
                        output += strs[0][n]
                        n += 1
            m += 1
        return output


s = Solution()
print(s.longestCommonPrefix(strs = []))
