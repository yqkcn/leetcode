class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if k == len(num):
            return "0"
        stack = []
        for letter in num:
            while stack and k and int(letter) < stack[-1]:
                stack.pop()
                k -= 1
            stack.append(int(letter))
        # 如果 k > 0,表示未删除足够的字符
        if k > 0:
            stack = stack[:-k]
        return "".join(str(x) for x in stack).lstrip("0") or "0"
