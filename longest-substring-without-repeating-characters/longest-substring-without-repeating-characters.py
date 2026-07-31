class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        window = {}
        best = 0
        for right in range(0, len(s)):
            ch = s[right]
            window[ch] = window.get(ch, 0) + 1
            while window[s[right]] > 1:
                window[s[left]] -= 1
                if window[s[left]] == 0:
                    del window[s[left]]
                left+=1
            if len(window) > best:
                best = max(best, right - left + 1)
        return best