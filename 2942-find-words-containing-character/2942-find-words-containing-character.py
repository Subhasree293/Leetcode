class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        n = len(words)
        ans = []
        for i in range(n):
            if x in words[i]:
                ans.append(i)
        
        return ans