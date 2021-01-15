"""
Two Sum (Leetcode problem #1)
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]

Constraints:
    2 <= nums.length <= 10^3
    -10^9 <= nums[i] <= 10^9
    -10^9 <= target <= 10^9
    Only one valid answer exists.

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
"""
class Solution:
    def twoSum(self, nums, target):
        r = 1
        n = 0
        y = r
        while True:
            if nums[n] + nums[y] == target:
                return [n,y]
                break
            else:
                n = n + 1
                y = y + 1
                #print("First: r=", r, "n=", n, "y=", y)
                if y == len(nums):
                    r = r + 1
                    n = 0
                    y = r
                    #print("Second: r=", r, "n=", n, "y=", y)

s = Solution()
print(s.twoSum(nums=[3,2,9,10,23,14], target=6))
