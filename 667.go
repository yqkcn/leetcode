package main

func constructArray(n int, k int) []int {
	var res []int
	for i := 1; i <= n-k-1; i++ {
		res = append(res, i)
	}
	left, right := n-k, n
	for left <= right {
		if left == right {
			res = append(res, left)
			break
		}
		res = append(res, left)
		res = append(res, right)
		left++
		right--
	}
	return res
}
