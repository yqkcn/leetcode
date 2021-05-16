package main

func createTargetArray(nums []int, index []int) []int {
	var target []int
	for i, num := range nums {
		target = append(target, 0)
		copy(target[index[i]+1:], target[index[i]:])
		target[index[i]] = num
	}
	return target
}
