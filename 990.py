from typing import List


class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        if not equations:
            return True
        flag = True
        while flag:
            flag = False
            for e in equations:
                char_1, operator, char_2 = e[0], e[1:3], e[3]
                if char_1 == char_2:
                    if operator == "!=":
                        return False
                    continue
                if operator == "!=":
                    continue
                equations = [_.replace(char_2, char_1) for _ in equations]
                flag = True
        return True

if __name__ == '__main__':
    s = Solution()
    print(s.equationsPossible(["a==b", "b!=a"]))
    print(s.equationsPossible(["b==a","a==b"]))
    print(s.equationsPossible(["a==b","b==c","a==c"]))
    print(s.equationsPossible(["a==b","b!=c","c==a"]))
    print(s.equationsPossible(["c==c","b==d","x!=z"]))
    print(s.equationsPossible(["c==c","f!=a","f==b","b==c"]))
    print(s.equationsPossible(["e==d","e==a","f!=d","b!=c","a==b"]))
