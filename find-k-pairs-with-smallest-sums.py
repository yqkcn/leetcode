from typing import List


class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        answer = []
        for n1 in nums1[:k]:
            for n2 in nums2[:k]:
                answer.append([n1, n2])
        answer.sort(key=lambda x: x[0] + x[1])
        return answer[:k]


class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        import heapq
        m, n = len(nums1), len(nums2)
        queue = [(nums1[0] + nums2[0], 0, 0)]
        heapq.heapify(queue)
        answer = []
        while queue and len(answer) < k:
            _, i, j = heapq.heappop(queue)
            answer.append([nums1[i], nums2[j]])
            # 右边邻居
            if j < n - 1:
                heapq.heappush(queue, (nums1[i] + nums2[j + 1], i, j + 1))
            # 下边邻居
            if j == 0 and i < m - 1:
                heapq.heappush(queue, (nums1[i + 1] + nums2[0], i + 1, 0))
        return answer
