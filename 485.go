package main

func findMaxConsecutiveOnes(nums []int) int {
	maxNum := 0
	curMaxNum := 0
	for _, num := range nums {
		if num == 1 {
			curMaxNum += 1
		} else {
			if curMaxNum > maxNum {
				maxNum = curMaxNum
			}
			curMaxNum = 0
		}
	}
	if curMaxNum != 0 {
		if curMaxNum > maxNum {
			maxNum = curMaxNum
		}
	}
	return maxNum
}
