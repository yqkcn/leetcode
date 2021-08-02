class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        for letter in s:
            if letter == " ":
                continue
            elif letter == "(":
                stack.append(letter)
            elif letter in "+-":
                stack.append(letter)
            elif letter.isdigit():
                if not stack:
                    stack.append(int(letter))
                elif stack[-1] == "+":
                    stack.pop()
                    stack.append(int(letter))
                elif stack[-1] == "-":
                    stack.pop()
                    stack.append(-1 * int(letter))
                elif stack[-1] == "(":
                    stack.append(int(letter))
                else:
                    if stack[-1] >= 0:
                        stack[-1] = stack[-1] * 10 + int(letter)
                    else:
                        stack[-1] = stack[-1] * 10 - int(letter)
            elif letter == ")":
                cur = []
                while stack:
                    item = stack.pop()
                    if item == "(":
                        break
                    cur.append(item)
                cur = sum(cur)
                if not stack:
                    stack.append(cur)
                elif stack[-1] == "+":
                    stack.pop()
                    stack.append(cur)
                elif stack[-1] == "-":
                    stack.pop()
                    stack.append(-1 * cur)
        return sum(stack)


if __name__ == '__main__':
    print(Solution().calculate("-(2 + 1 -6)"))
