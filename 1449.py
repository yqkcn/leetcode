# 给你一个整数数组 cost 和一个整数 target 。请你返回满足如下规则可以得到的 最大 整数：
#
# 给当前结果添加一个数位（i + 1）的成本为 cost[i] （cost 数组下标从 0 开始）。
# 总成本必须恰好等于 target 。
# 添加的数位中没有数字 0 。
# 由于答案可能会很大，请你以字符串形式返回。
#
# 如果按照上述要求无法得到任何整数，请你返回 "0" 。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/form-largest-integer-with-digits-that-add-up-to-target
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
from typing import List


def largestNumber(cost: List[int], target: int) -> str:
    res = "0"
    deque = [("", target)]
    while deque:
        print(deque)
        cur, num = deque.pop()
        for i in range(1, 10):
            _str = "{}{}".format(cur, i)
            _num = num - cost[i - 1]
            if _num < 0 or "0" in _str:
                continue
            # 删除无效的任务
            _temp = cur
            processed = set()
            for _ in deque:
                if _[1] == _num:
                    processed.add(_)
                _temp = cur if (cur and _[0] and  int(cur) >= int(_[0])) else _[0]
            deque = [_ for _ in deque if _ not in processed]
            deque.append((_temp, _num))
            if _num == 0:
                processed.add((_str, _num))
                if int(_str) > int(res):
                    res = _str
                continue
            deque.append((_str, _num))
    return res


if __name__ == '__main__':
    for cost, target in [
        ([4, 3, 2, 5, 6, 7, 2, 5, 5], 9),
        ([7, 6, 5, 5, 5, 6, 8, 7, 8], 12),
        ([2, 4, 6, 2, 4, 6, 4, 4, 4], 5),
        ([6, 10, 15, 40, 40, 40, 40, 40, 40], 47),
        ([1, 1, 1, 1, 1, 1, 1, 3, 2], 10),
        ([6,10,15,53,43,53,51,47,43], 89),
    ][-1:]:
        print(largestNumber(cost, target))
