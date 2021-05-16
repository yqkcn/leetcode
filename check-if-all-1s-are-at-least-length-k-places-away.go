package main

func kLengthApart(nums []int, k int) bool {
	pre := -1
	for i, num := range nums {
		if num == 1 {
			if pre == -1 {
				pre = i
			} else {
				if i-pre <= k {
					return false
				} else {
					pre = i
				}
			}
		}
	}
	return true
}
