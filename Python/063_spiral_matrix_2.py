# Given a positive integer n, generate an n x n matrix filled with elements from 1 to n2 in spiral order.

# Example 1:
# Input: n = 3
# Output: [[1,2,3],[8,9,4],[7,6,5]]

# Example 2:
# Input: n = 1
# Output: [[1]]

# Constraints:
# 1 <= n <= 20

class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        if not n:
            return []
        result = [[0 for _ in range(n)] for _ in range(n)]
        left, right, top, down, num = 0, n-1, 0, n-1, 1
        while left <= right and top <= down:
            for i in range(left, right+1):
                result[top][i] = num 
                num += 1
            top += 1
            for i in range(top, down+1):
                result[i][right] = num
                num += 1
            right -= 1
            for i in range(right, left-1, -1):
                result[down][i] = num
                num += 1
            down -= 1
            for i in range(down, top-1, -1):
                result[i][left] = num
                num += 1
            left += 1
        return result