class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        if sentence1 == sentence2:
            return True
        s1, s2 = sentence1.split(" "), sentence2.split(" ")
        while s1 and s2:
            if s1[0] == s2[0]:
                s1, s2 = s1[1:], s2[1:]
            elif s1[-1] == s2[-1]:
                s1, s2 = s1[:-1], s2[:-1]
            else:
                break
        return not s1 or not s2