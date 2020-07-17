package main

import "fmt"

func largestRectangleArea(heights []int) int {
	if heights == nil {
		return 0
	}
	if len(heights) == 1 {
		return heights[0]
	}
	max := 0
	for i := 0; i < len(heights); i++ {
		minNUm := heights[i]
		for j := i; j >= 0; j-- {
			if heights[j] <= minNUm {
				minNUm = heights[j]
			}
			// 最矮的那个决定面积
			area := minNUm * (i - j + 1)
			if area > max {
				max = area
			}
		}
	}
	return max
}

func main() {
	fmt.Print(largestRectangleArea([]int{2, 1, 5, 6, 2, 3}))
}
