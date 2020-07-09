package main

func main() {
	removeDuplicates([]int{0,0,1,1,1,1,2,3,3})
}

func removeDuplicates(nums []int) int {
	if len(nums) <= 2 {
		return len(nums)
	}
	i, k := 1, 1
	for j := 1; j < len(nums); j++ {
		if nums[j] == nums[i-1] {
			if k == 2 {
				continue
			}
			nums[i] = nums[j]
			k += 1
			i += 1
		} else {
			nums[i] = nums[j]
			k = 1
			i += 1
		}
	}
	return i
}
