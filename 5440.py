# 给你两个整数，n 和 start 。
# 数组 nums 定义为：nums[i] = start + 2*i（下标从 0 开始）且 n == nums.length 。
# 请返回 nums 中所有元素按位异或（XOR）后得到的结果。
def xorOperation(n: int, start: int) -> int:
    res = 0
    for i in range(n):
        res ^= start + 2*i
    return res

if __name__ == '__main__':
    print(xorOperation(5, 0))
    print(xorOperation(4, 3))
    print(xorOperation(1, 7))
    print(xorOperation(10, 5))