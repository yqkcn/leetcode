import collections
from typing import List


class MagicDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = collections.defaultdict(set)

    def buildDict(self, dictionary: List[str]) -> None:
        for word in dictionary:
            self.data[len(word)].add(word)

    def search(self, searchWord: str) -> bool:
        for word in self.data[len(searchWord)]:
            if len([x for x in range(len(searchWord)) if word[x] != searchWord[x]]) == 1:
                return True
        return False

# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)
