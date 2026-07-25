class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for i in nums:
                freq[i] = freq.get(i, 0) + 1
                
        freq_elements = []
        while len(freq_elements) < k:
            best_key  = None
            best_value = -1
            for i, val in freq.items():
                if val > best_value:
                    best_key = i
                    best_value = val
            freq_elements.append(best_key)
            del freq[best_key]
        return freq_elements