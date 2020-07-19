package main

import "math"

func constructRectangle(area int) []int {
	mid := int(math.Ceil(math.Sqrt(float64(area))))
	if mid*mid == area {
		return []int{mid, mid}
	}
	res := []int{area, 1}
	for w := 1; w <= mid; w++ {
		for l := mid; l < area; l++ {
			if w*l > area {
				break
			}
			if w*l == area {
				if l-w < res[0]-res[1] {
					res[0] = l
					res[1] = w
				}
			}
		}
	}
	return res
}
