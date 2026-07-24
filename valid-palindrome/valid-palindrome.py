class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        letters = [letter for letter in s if letter.isalnum()]
        r = len(letters) - 1
        l = 0

        while l < r:
            if(letters[l] != letters[r]):
                return False
            else:
                r-=1
                l+=1
        return True


