package main

import (
	"fmt"
	"sort"
)

func wiggleSort2(nums []int) {
	sort.Ints(nums)
	var res []int
	left, right := 0, len(nums)-1
	for left < right {
		res = append(res, nums[left])
		res = append(res, nums[right])
		left++
		right--
	}
	if left == right {
		res = append(res, nums[left])
	}
	copy(nums, res)
	fmt.Printf("%v", nums)
}

func main() {
	nums := []int{5, 3, 1, 2, 3}
	wiggleSort2(nums)
}