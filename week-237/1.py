class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        import string

        for i in string.ascii_lowercase:
            if i not in sentence:
                return False
        return True