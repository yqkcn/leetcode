package main


func moveZeroes(nums []int)  {
	right := len(nums) - 1
	for right >= 0 {
		if nums[right] == 0 {
			right --
		} else {
			break
		}
	}
	if right <= 0 {
		return
	}
	left := 0
	for left < right {
		if left == right {
			break
		}
		if nums[left] == 0 {
			if left == len(nums) - 2 {
				nums[left], nums[right] = nums[right], nums[left]
				return
			}
			tmp := nums[left]
			copy(nums[left:right], nums[left+1:right+1])
			nums[right] = tmp
			right--
		} else {
			left++
		}
	}
}
