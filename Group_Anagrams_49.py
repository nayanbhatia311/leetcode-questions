from collections import defaultdict
class Solution:
    def countFrom0(self,ch: int):
        return ord(ch)-ord("a")
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap=defaultdict(list)

        for word in strs:
            bitmask_ch = [0]*26
            for ch in word:
                bitmask_ch[self.countFrom0(ch)] +=1
            hashmap[tuple(bitmask_ch)].append(word)
        return(list(hashmap.values()))
