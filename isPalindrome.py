# https://leetcode.com/problems/valid-palindrome/

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        letters = {"a": "a",
                   "b": "b",
                   "c": "c",
                   "d": "d",
                   "e": "e",
                   "f": "f",
                   "g": "g",
                   "h": "h",
                   "i": "i",
                   "j": "j",
                   "k": "k",
                   "l": "l",
                   "m": "m",
                   "n": "n",
                   "o": "o",
                   "p": "p",
                   "q": "q",
                   "r": "r",
                   "s": "s",
                   "t": "t",
                   "u": "u",
                   "v": "v",
                   "w": "w",
                   "x": "x",
                   "y": "y",
                   "z": "z",
                   "0": "A",
                   "1": "1",
                   "2": "2",
                   "3": "3",
                   "4": "4",
                   "5": "5",
                   "6": "6",
                   "7": "7",
                   "8": "8",
                   "9": "9",
                  }
        
        temp = []
        
        for char in lower(s):
            if char in letters:
                temp.append(char)
        
        left, right = 0, len(temp) - 1
        while left < right:
            if temp[left] != temp[right]:
                return False
            left += 1
            right -= 1
            
        return True