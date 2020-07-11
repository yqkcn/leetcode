package main

import "fmt"

func countSmaller(nums []int) []int {
	var res []int
	for i := 0; i < len(nums); i++ {
		res = append(res, 0)
	}
	if len(nums) < 2 {
		return res
	}
	for i := len(nums) - 1; i >= 0; i-- {
		if i == len(nums)-1 {
			continue
		}
		num := 0
		for j := i + 1; j < len(nums); j++ {
			if nums[j] < nums[i] {
				num += 1
			}
			if nums[j] == nums[i] {
				num += res[j]
				break
			}
		}
		res[i] = num
	}
	return res
}

func main() {
	fmt.Print(countSmaller([]int{5, 2, 6, 1}))
}
