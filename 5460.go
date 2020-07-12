package main

import "fmt"

func numIdenticalPairs(nums []int) int {
	res := 0
	if len(nums) < 2 {
		return res
	}
	for i := 0; i < len(nums)-1; i++ {
		for j := i + 1; j < len(nums); j++ {
			if nums[i] == nums[j] {
				res += 1
			}
		}
	}
	fmt.Print(res)
	return res
}

func main() {
	numIdenticalPairs([]int{1, 2, 3, 1, 1, 3})
	numIdenticalPairs([]int{1, 1, 1, 1})
	numIdenticalPairs([]int{1, 2, 3})
}
