class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        for letter in s:
            if letter != ")":
                stack.append(letter)
                continue
            cur = []
            while stack and stack[-1] != "(":
                cur.append(stack.pop()[::-1])
            stack.pop()
            stack.append("".join(cur))
        return "".join(stack)


if __name__ == '__main__':
    print(Solution().reverseParentheses("a(bcdefghijkl(mno)p)q"))
