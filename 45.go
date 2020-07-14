package main

func jump(nums []int) int {
	if len(nums) < 2 {
		return 0
	}
	res := 0
	cache := make(map[int]bool)
	steps := [][]int{{0, 0}}
	for len(steps) != 0 {
		// 两个整数，第一个是步数，第二个是当前下标数
		cur := steps[0]
		steps = steps[1:]
		// 已经跳到过，不处理
		if cache[cur[1]] {
			continue
		}
		// 到达最后一步
		if cur[1] == len(nums)-1 {
			res = cur[0]
			break
		}
		cache[cur[1]] = true
		if cur[1]+nums[cur[1]] >= len(nums)-1 {
			res = cur[0] + 1
			break
		}
		// cur[1] 步之内的全部加入队列，逆序添加比较快
		for i := nums[cur[1]]; i >= 1; i-- {
			steps = append(steps, []int{cur[0] + 1, cur[1] + i})
		}
	}
	return res
}

func main() {
	jump([]int{2, 3, 1, 1, 4})
}
