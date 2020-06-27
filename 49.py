from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        import collections
        res = collections.defaultdict(list)
        for _str in strs:
            sort_str = "".join(sorted(list(_str)))
            res[sort_str].append(_str)
        return list(res.values())


if __name__ == '__main__':
    s = Solution()
    print(s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
