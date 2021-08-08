class Solution:
    def minSwaps(self, s: str) -> int:
        stack = []
        for i in s:
            if i == "[":
                stack.append(i)
            else:
                if stack and stack[-1] == "[":
                    stack.pop()
                else:
                    stack.append(i)
        num = len(stack) // 2
        a, b = num // 2, num % 2
        if b :
            a += 1
        return a
