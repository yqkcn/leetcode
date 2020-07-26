package main

import (
	"sort"
)

func wiggleSort(nums []int) {
	sort.Ints(nums)
	if len(nums) < 2 {
		return
	}
	if len(nums) == 3 {
		nums[1], nums[2] = nums[2], nums[1]
		return
	}
	left, right := 1, len(nums)-2
	for left < right {
		nums[left], nums[right] = nums[right], nums[left]
		left += 2
		right -= 2
	}
}

func main() {
	wiggleSort([]int{1,2,3})
}