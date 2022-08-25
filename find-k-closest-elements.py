class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        idx = bisect.bisect_left(arr, x)
        res = []
        left, right = idx - 1, idx
        while len(res) < k:
            num1 = None if left < 0 else arr[left]
            num2 = None if right >= len(arr) else arr[right]
            if num1 is not None and num2 is not None:
                if abs(num1 - x) <= abs(num2 - x):
                    res.insert(0, num1)
                    left -= 1
                else:
                    res.append(num2)
                    right += 1
                continue
            if num1 is not None:
                res.insert(0, num1)
                left -= 1
                continue
            res.append(num2)
            right += 1
        return res