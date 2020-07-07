from typing import List


class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        # 字符串为空，或者本身括号已经有效，不需要去除，直接返回
        if not s or self.is_invalid(s):
            return [s]
        # 找到有效括号对数
        invalid_number = self.get_invalid_number(s)
        m = s.count("(") - invalid_number
        n = s.count(")") - invalid_number
        res = []
        if not m and not n:
            return [s]
        # 只用替换左括号
        if not n and m:
            for sub_left in self.sub_left(s, 0, m):
                if self.is_invalid(sub_left):
                    res.append(sub_left)
        elif not m and n:
            for sub_right in self.sub_right(s, 0, n):
                if self.is_invalid(sub_right):
                    res.append(sub_right)
        else:
            for sub_left in self.sub_left(s, 0, m):
                for sub_right in self.sub_right(sub_left, 0, n):
                    if self.is_invalid(sub_right):
                        res.append(sub_right)
        return list(set(_.replace("0", "").replace("1", "") for _ in res))

    def sub_left(self, s, idx, num) -> List[str]:
        """ 替换掉字符串中 num 个左括号 """
        if num == 0:
            return [s]
        res = []
        for i, char in enumerate(s[idx:], idx):
            if char == "(":
                _s = s[:i] + "0" + s[i + 1:]
                res.extend(self.sub_left(_s, i + 1, num - 1))
        return res

    def sub_right(self, s, idx, num) -> List[str]:
        """ 替换掉字符串中 num 个右括号 """
        if num == 0:
            return [s]
        res = []
        for i, char in enumerate(s[idx:], idx):
            if char == ")":
                _s = s[:i] + "1" + s[i + 1:]
                res.extend(self.sub_right(_s, i + 1, num - 1))
        return res

    def is_invalid(self, s: str) -> bool:
        """ 判断字符串括号是都都有效 """
        stack = []
        for i in s:
            if i == "(":
                stack.append("(")
            elif i == ")":
                if stack:
                    stack.pop()
                else:
                    return False
        if stack:
            return False
        return True

    def get_invalid_number(self, s: str) -> int:
        """ 获取字符串经过删减得到的最多有效括号对数 """
        if not s:
            return 0
        stack = []
        res = 0
        for i in s:
            if i == "(":
                stack.append("(")
            elif i == ")":
                if stack:
                    stack.pop()
                    res += 1
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.removeInvalidParentheses("()())()"))
    print(s.removeInvalidParentheses("(a)())()"))
    print(s.removeInvalidParentheses(")("))
    print(s.removeInvalidParentheses("("))
