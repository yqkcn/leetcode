package main

func rotate(nums []int, k int) {
	k = k % len(nums)
	for k > 0 {
		tmp := nums[len(nums)-1]
		copy(nums[1:], nums[:len(nums)-1])
		nums[0] = tmp
		k--
	}
}
