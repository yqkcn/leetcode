def least_money():
    """
    输入
    第一行有五个数，分别为d1，c，d2，m，n。
    接下来n行，每行两个数dｉ与pｉ，分别表示第ｉ号油站离出发点的距离与该油站每升汽油的价格。
    输出
    如果可以送到，则输出一个数，表示最小费用。保留两位小数。如果不能，则输出“No Solution”。
    """
    d1, c, d2, m, n = [float(x) for x in input("输入第一行").split()]
    n = int(n)
    stations = [(0, m)]
    while a := input("请输入站点"):
        u, v = list(filter(lambda x: x.strip(), a.split(" ")))
        stations.append((float(u), float(v)))
    # 排序
    stations.sort(key=lambda x: x[0])
    ans = float("inf")
    length = len(stations)
    # 加油站编号， 油箱里容量， 累计花费
    queue = [(0, 0, 0)]
    # 跑的最远
    longest = c * d2
    # 搜索
    while queue:
        idx, cur, total = queue.pop(0)
        # 到达目的地
        if idx == length - 1:
            ans = min(ans, total)
            continue
        # 从当前加油站可以到达的所有加油站
        e, f = stations[idx]
        for i in range(idx + 1, length):
            x, y = stations[i]
            # 到达不了
            if x - e > longest:
                break
            # 需要保证每次加油之后，邮箱里的油不能超过目的地
            # 下一个加油站比当前加油站贵
            if y >= f:
                # 在当前加油站加最大值，加完之后不能超越终点
                if e + longest > d1:
                    z = (d1 - e) / d2
                    queue.append((i, z - (x - e) / d2, total + f * (z - cur)))
                # 到不了终点站， 加满
                else:
                    queue.append((i, c - (x - e) / d2, total + f * (c - cur)))
                continue
            # 下一个加油站比当前加油站便宜
            # 只保证邮箱里的油能跑到下一个加油站即可
            if cur * d2 >= x - e:
                queue.append((i, cur - (x - e) / d2, total))
            # 加到正好
            else:
                queue.append((i, 0, total + (x - e - cur * d2) / d2 * f))
    if ans == float("inf"):
        print("No Solution")
    else:
        print(ans)


if __name__ == '__main__':
    least_money()
