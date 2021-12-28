class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        # 缓存处理结果
        self.cache = {}
        # 构造前缀树
        trie = Trie()
        for word in words:
            if not word:
                continue
            trie.insert(word)
        self.trie = trie
        ans = []
        # print(self.trie.search_prefix("cats", allow_same=True))
        for word in words:
            if not word:
                continue
            # print(word, self.search(word))
            if self.search(word, allow_same=False):
                ans.append(word)
        return ans

    def search(self, word, allow_same=False) -> bool:
        if not word:
            return True
        if allow_same and word in self.cache:
            return self.cache[word]
        # print(word, self.trie.search_prefix(word, allow_same=allow_same))
        for prefix in self.trie.search_prefix(word, allow_same=allow_same):
            if self.search(word[len(prefix):], allow_same=True):
                self.cache[word] = True
                return True
        if allow_same:
            self.cache[word] = False
        return False


class Trie(object):
    """前缀树"""

    def __init__(self):
        self.children = {}  # 用于保存子节点
        self.val = None

    def insert(self, word: str) -> None:
        """插入一个元素"""
        node = self
        for ch in word:
            if ch not in node.children:
                node.children[ch] = Trie()
            node = node.children[ch]
        node.val = word

    def search_prefix(self, word: str, allow_same=False) -> list[str]:
        """查询是否有元素是给定 word 的前缀"""
        ans = []
        node = self
        for ch in word:
            if ch not in node.children:
                return ans
            node = node.children[ch]
            if node.val:
                if allow_same or node.val != word:
                    ans.append(node.val)
        return ans

