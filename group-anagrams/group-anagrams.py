class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ang = {}
        
        for words in strs:
            key = tuple(sorted(words))

            if key not in ang:
                ang[key] = []
            
            ang[key].append(words)
        return list(ang.values())






