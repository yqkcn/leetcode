package main

func findLengthOfLCIS(nums []int) int {
	length := len(nums)
	if length <= 1 {
		return length
	}
	res, l, r := 1, 0, 1
	for r < length {
		if nums[r] > nums[r-1] {
			r++
			if (r - l) > res {
				res = r - l
			}
		} else {
			l, r = r, r+1
		}
	}
	return res
}

func main() {
	findLengthOfLCIS([]int{1, 3, 5, 4, 7})
}
