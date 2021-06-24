class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        pre = None
        stack = []
        num = 0
        for ch in dominoes:
            if ch == ".":
                num += 1
            elif ch == "L":
                if not pre or ch == pre:
                    stack.extend([ch] * (num + 1))
                else:
                    a, b = num // 2, num % 2
                    if not b:
                        stack.extend([pre] * a)
                        stack.extend([ch] * (a + 1))
                    else:
                        stack.extend([pre] * a)
                        stack.append(".")
                        stack.extend([ch] * (a + 1))
                pre = ch
                num = 0
            else:
                if not pre or ch != pre:
                    stack.extend(["."] * num)
                    stack.append(ch)
                else:
                    stack.extend([ch] * (num + 1))
                pre = ch
                num = 0
        if num:
            ch = "R" if pre == "R" else "."
            stack.extend([ch] * num)
        return "".join(stack)
