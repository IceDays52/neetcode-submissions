class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = []

        for i in range(min(len(word1), len(word2))):
            res.append(word1[i])
            res.append(word2[i])

        res.extend(word1[i + 1:])
        res.extend(word2[i + 1:])

        return "".join(res)