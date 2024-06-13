# Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:
# 0 <= a, b, c, d < n
# a, b, c, and d are distinct.
# nums[a] + nums[b] + nums[c] + nums[d] == target
# You may return the answer in any order.

# Example 1:
# Input: nums = [1,0,-1,0,-2,2], target = 0
# Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]

# Example 2:
# Input: nums = [2,2,2,2,2], target = 8
# Output: [[2,2,2,2]]
 
# Constraints:
# 1 <= nums.length <= 200
# -109 <= nums[i] <= 109
# -109 <= target <= 109

class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if len(nums) <= 3:
            return []

        nums.sort()
        s = set()
        output = []
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                k = j + 1
                l = len(nums) - 1
                while k < l:
                    sum = nums[i] + nums[j] + nums[k] + nums[l]
                    if sum == target:
                        s.add((nums[i], nums[j], nums[k], nums[l]))
                        k += 1
                        l -= 1
                    elif sum < target:
                        k += 1
                    else:
                        l -= 1
        output = list(s)
        return output