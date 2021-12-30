class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        import collections
        counter = collections.defaultdict(int)
        for num in arr:
            counter[num % k] += 1
        keys = list(sorted(counter.keys()))
        for key in keys:
            if key == 0:
                continue
            a = k - key
            # 自身
            if a == key:
                if counter[key] % 2:
                    return False
                continue
            # 找对象
            if a not in counter or counter[key] != counter[a]:
                return False
        return True
