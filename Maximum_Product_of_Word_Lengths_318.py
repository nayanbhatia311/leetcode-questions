from collections import defaultdict
class Solution:

    def index0(self, ch: str) -> int:
        return ord(ch)-ord('a')
    def maxProduct(self, words: List[str]) -> int:
        hashmap=defaultdict(int)
        for word in words:
            bitmap=0
            for ch in word:
                bitmap |= 1<< self.index0(ch)
            hashmap[bitmap]=max(hashmap[bitmap],len(word))
        length=0
        for bits in hashmap:
            for bits2 in hashmap:
                if bits & bits2 == 0:
                    length=max(length,hashmap[bits]*hashmap[bits2])

        return length
