# Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.
# Each number in candidates may only be used once in the combination.
# Note: The solution set must not contain duplicate combinations.

# Example 1:
# Input: candidates = [10,1,2,7,6,1,5], target = 8
# Output: 
# [
# [1,1,6],
# [1,2,5],
# [1,7],
# [2,6]
# ]

# Example 2:
# Input: candidates = [2,5,2,1,2], target = 5
# Output: 
# [
# [1,2,2],
# [5]
# ]

# Constraints:
# 1 <= candidates.length <= 100
# 1 <= candidates[i] <= 50
# 1 <= target <= 30

class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = []
        candidates.sort()
        if len(candidates) == 0:
            return
        def helper(candidates, path, result, target):
            if target < 0:
                return
            elif target == 0:
                result.append(path)
                return
            else:
                for i in range(len(candidates)):
                    if i > 0 and candidates[i] == candidates[i - 1]:
                        continue
                    if candidates[i] > target:
                        continue
                    helper(candidates[i + 1:], path + [candidates[i]], result, target - candidates[i])
        helper(candidates, [], result, target)
        return result