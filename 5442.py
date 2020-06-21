# 你的国家有无数个湖泊，所有湖泊一开始都是空的。当第 n 个湖泊下雨的时候，如果第 n 个湖泊是空的，那么它就会装满水，否则这个湖泊会发生洪水。你的目标是避免任意一个湖泊发生洪水。
# 给你一个整数数组 rains ，其中：
# rains[i] > 0 表示第 i 天时，第 rains[i] 个湖泊会下雨。
# rains[i] == 0 表示第 i 天没有湖泊会下雨，你可以选择 一个 湖泊并 抽干 这个湖泊的水。
# 请返回一个数组 ans ，满足：
# ans.length == rains.length
# 如果 rains[i] > 0 ，那么ans[i] == -1 。
# 如果 rains[i] == 0 ，ans[i] 是你第 i 天选择抽干的湖泊。
# 如果有多种可行解，请返回它们中的 任意一个 。如果没办法阻止洪水，请返回一个 空的数组 。
# 请注意，如果你选择抽干一个装满水的湖泊，它会变成一个空的湖泊。但如果你选择抽干一个空的湖泊，那么将无事发生（详情请看示例 4）
from typing import List


def avoidFlood(rains: List[int]) -> List[int]:
    avalid = []
    res = []
    full = {}
    for i, rain in enumerate(rains):
        res.append(-1)
        if rain == 0:
            avalid.append(i)
            continue
        # 下雨，并且之前为空
        if rain not in full:
            full[rain] = i
            continue
        # 下雨，之前满了，尝试提前抽空
        if not avalid:
            return []
        _flag = False
        for _idx in avalid:
            if full[rain] < _idx < i:
                res[_idx] = rain
                avalid.remove(_idx)
                full[rain] = i
                _flag = True
                break
        if not _flag:
            return []

    if avalid:
        for _idx in avalid:
            res[_idx] = 1
    return res


if __name__ == '__main__':
    # print(avoidFlood([1,2,3,4]))
    # print(avoidFlood([1,2,0,0,2,1]))
    # print(avoidFlood([1,2,0,1,2]))
    # print(avoidFlood([69,0,0,0,69]))
    # print(avoidFlood([10,20,20]))
    # print(avoidFlood([0,1,1]))
    print(avoidFlood([2,3,0,0,3,1,0,1,0,2,2]))