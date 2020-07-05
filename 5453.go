package main

//有一块木板，长度为 n 个 单位 。一些蚂蚁在木板上移动，每只蚂蚁都以 每秒一个单位 的速度移动。其中，一部分蚂蚁向 左 移动，其他蚂蚁向 右 移动。
//当两只向 不同 方向移动的蚂蚁在某个点相遇时，它们会同时改变移动方向并继续移动。假设更改方向不会花费任何额外时间。
//而当蚂蚁在某一时刻 t 到达木板的一端时，它立即从木板上掉下来。
//给你一个整数 n 和两个整数数组 left 以及 right 。两个数组分别标识向左或者向右移动的蚂蚁在 t = 0 时的位置。请你返回最后一只蚂蚁从木板上掉下来的时刻。
func getLastMoment(n int, left []int, right []int) int {
	_left := 0
	if len(left) != 0 {
		_left = Max(left)
	}
	_right := 0
	if len(right) != 0 {
		_right = n - Min(right)
	}
	if _left > _right {
		return _left
	}
	return _right
}

func Max(nums []int) int {
	if len(nums) == 0 {
		return 0
	}
	if len(nums) == 1 {
		return nums[0]
	}
	res := 0
	for _, r := range nums {
		if r > res {
			res = r
		}
	}
	return res
}

// Min returns the smaller of x or y.
func Min(nums []int) int {
	if len(nums) == 0 {
		return 0
	}
	if len(nums) == 1 {
		return nums[0]
	}
	res := 0
	for _, r := range nums {
		if r < res {
			res = r
		}
	}
	return res
}

func intInSlice(n int, nums []int) bool {
	for _, num := range nums {
		if num == n {
			return true
		}
	}
	return false
}
