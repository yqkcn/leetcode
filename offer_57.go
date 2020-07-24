package main

func twoSum(nums []int, target int) []int {
	left, right := 0, len(nums)-1
	for left < right {
		cur := nums[left] + nums[right]
		if cur == target {
			return []int{nums[left], nums[right]}
		} else if cur > target {
			right--
		} else {
			left++
		}
	}
	return []int{}
}
