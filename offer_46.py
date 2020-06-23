class Solution:
    def translateNum(self, num: int) -> int:
        _str = str(num)
        if len(_str) == 1:
            return 1
        if len(_str) == 2:
            return 1 if num > 25 else 2
        num_1 = 1
        num_2 = 1 if int(_str[:2]) > 25 else 2
        for i, _num in enumerate(_str[2:], 2):
            # 当前数字可以和上一个数字结合
            if _str[i-1] != "0" and int(_str[i - 1:i + 1]) <= 25:
                num_1, num_2 = num_2, num_2 + num_1
            else:
                num_1, num_2 = num_2, num_2
        return num_2


if __name__ == '__main__':
    s = Solution()
    print(s.translateNum(12258))
    print(s.translateNum(1))
    print(s.translateNum(11))
    print(s.translateNum(26))
    print(s.translateNum(25))
    print(s.translateNum(506))
