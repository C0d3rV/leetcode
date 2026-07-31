class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        window  = {}
        best = 0
        for right in range(0, len(s)):
            c = s[right]
            window[c] = window.get(c, 0)+1
            max_freq = max(window.values())
            window_len = right-left+1
            while window_len - max_freq > k:
                window[s[left]] -= 1
                if window[s[left]] == 0:
                    del window[s[left]]
                left += 1
                window_len = right  - left + 1
                max_freq = max(window.values())
            best = max(best, right-left+1)
        return best
                