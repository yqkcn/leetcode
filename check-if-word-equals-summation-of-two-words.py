class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        import string
        _map = {k: str(i) for i, k in enumerate(string.ascii_lowercase)}
        num1 = int("".join(_map[x] for x in firstWord))
        num2 = int("".join(_map[x] for x in secondWord))
        num3 = int("".join(_map[x] for x in targetWord))
        return num1 + num2 == num3
