package main

func maxSlidingWindow(nums []int, k int) []int {
	if len(nums) == 0 {
		return []int{}
	}
	dq := []int{max(nums[:k])}
	for i := 0; i < len(nums)-k; i++ {
		// 窗口往前移动一位，判断最左侧是不是最大值
		if nums[i] == dq[i] {
			dq = append(dq, max(nums[i+1:i+k+1]))
		} else {
			dq = append(dq, max([]int{dq[i], nums[i+k]}))
		}
	}
	return dq
}

func max(nums []int) int {
	if len(nums) == 1 {
		return nums[0]
	}
	a, b := nums[0], max(nums[1:])
	if a > b {
		return a
	}
	return b
}
