import re

class Solution(object):
    def isPalindrome(self, s):

        newWord = s.replace(" ", "").lower()
        newWord = re.sub(r'[^a-zA-Z0-9]', "", newWord)
        firstPart, lastPart = 0, len(newWord) - 1
        while firstPart < lastPart:
            if newWord[firstPart] != newWord[lastPart]:
                return False
            firstPart += 1
            lastPart -= 1
        
        return True


