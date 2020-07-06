package main

import "fmt"

func main() {
	nums := []int{1, 2, 3, 1, 2, 3}
	fmt.Print(containsNearbyDuplicate(nums, 2))

}

func containsNearbyDuplicate(nums []int, k int) bool {
	if len(nums) == 0 {
		return false
	}
	for i, num := range nums[:len(nums)-1] {
		for j := i + 1; j < len(nums) && j < i+k+1; j++ {
			if num == nums[j] {
				return true
			}
		}
	}
	return false
}
