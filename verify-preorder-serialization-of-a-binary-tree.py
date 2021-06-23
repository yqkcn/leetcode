class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        if preorder == "#":
            return True
        stack = []
        for ch in preorder.split(","):
            if ch == "#":
                # 栈为空错误
                if not stack:
                    return False
                # 栈顶元素不是 "#" 不处理
                if stack[-1] != "#":
                    stack.append(ch)
                    continue
                # 栈顶元素也是 #，说明某一个节点的左右子树都已经遍历完
                stack.pop()
                # 为空说明没有父节点，错误
                if not stack:
                    return False
                # 父节点已经检查完毕，将其设置为 #
                # 继续往上层检查
                stack[-1] = "#"
                while len(stack) >= 3 and stack[-1] == "#" and stack[-2] == "#":
                    stack = stack[:-3]
                    stack.append("#")
            else:
                stack.append(ch)
        return len(stack) == 1 and stack[0] == "#"
