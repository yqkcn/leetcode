from typing import List


class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        import collections
        # 单词列表去重
        new_words = []
        for word in wordlist:
            if word not in new_words:
                new_words.append(word)
        wordlist = new_words
        # 构建三个容器分别存储原始的，小写的，替换元音的
        word_set = set(wordlist)
        lower_words = collections.defaultdict(list)
        replaced_words = collections.defaultdict(list)
        for word in wordlist:
            lower_words[word.lower()].append(word)
            # 替换元音字母，获取所有的排雷组合
            letters_list = [[]]
            for letter in word.lower():
                # 将元音字母替换为 #
                letter = letter if letter not in "aeiou" else "#"
                for letters in letters_list:
                    letters.append(letter)
            # 组成单词
            for letters in letters_list:
                replaced_words["".join(letters)].append(word)
        result = []
        for query in queries:
            if query in word_set:
                result.append(query)
            elif query.lower() in lower_words:
                result.append(lower_words[query.lower()][0])
            elif (_query := query.lower().replace("a", "#").replace("e", "#").replace("i", "#").replace("o", "#").replace("u", "#")) in replaced_words:
                result.append(replaced_words[_query][0])
            else:
                result.append("")
        return result
