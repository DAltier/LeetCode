# Given an integer, convert it to a Roman numeral.

# Example 1:
# Input: num = 3749
# Output: "MMMDCCXLIX"
# Explanation:
# 3000 = MMM as 1000 (M) + 1000 (M) + 1000 (M)
#  700 = DCC as 500 (D) + 100 (C) + 100 (C)
#   40 = XL as 10 (X) less of 50 (L)
#    9 = IX as 1 (I) less of 10 (X)
# Note: 49 is not 1 (I) less of 50 (L) because the conversion is based on decimal places

# Example 2:
# Input: num = 58
# Output: "LVIII"
# Explanation:
# 50 = L
#  8 = VIII

# Example 3:
# Input: num = 1994
# Output: "MCMXCIV"
# Explanation:
# 1000 = M
#  900 = CM
#   90 = XC
#    4 = IV
 
# Constraints:
# 1 <= num <= 3999

class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        ones = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
        tens = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
        hnds = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
        thos = ["", "M", "MM", "MMM"]

        return thos[int(num / 1000)] + hnds[int((num % 1000) / 100)] + tens[int((num % 100) / 10)] + ones[int(num % 10)]