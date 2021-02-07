class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        res = ""
        idx1 = idx2 = 0
        while idx1 < len(word1) and idx2 < len(word2):
            if word1[idx1:] >= word2[idx2:]:
                res += word1[idx1]
                idx1 += 1
            elif word1[idx1:] < word2[idx2:]:
                res += word2[idx2]
                idx2 += 1
        if idx1 <= len(word1) - 1:
            res += word1[idx1:]
        if idx2 <= len(word2) - 1:
            res += word2[idx2:]
        return res


if __name__ == '__main__':
    a = Solution().largestMerge("cabaa", "bcaaa")
    print(a)
