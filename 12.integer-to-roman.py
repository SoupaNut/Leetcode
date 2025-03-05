#
# @lc app=leetcode id=12 lang=python3
#
# [12] Integer to Roman
#

# @lc code=start
class Solution:
    def intToRoman(self, num: int) -> str:
        translations = {
            1: "I",
            4: "IV",
            5: "V",
            9: "IX",
            10: "X",
            40: "XL",
            50: "L",
            90: "XC",
            100: "C",
            400: "CD",
            500: "D",
            900: "CM",
            1000: "M"
        }
        
        roman = ""
        
        if num // 1000 >= 1:
            roman += translations[1000] * (num // 1000)
            num %= 1000
        
        if num // 100 >= 1:
            roman += translations[100] * (num // 100)
            num %= 100
        
        if num // 10 >= 1:
            roman += translations[10] * (num // 10)
            num %= 10
        
# @lc code=end

