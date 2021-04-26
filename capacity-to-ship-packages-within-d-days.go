package main

import "fmt"

func shipWithinDays(weights []int, D int) int {
	left := Max(weights)
	right := Sum(weights)
	for left < right {
		fmt.Print(left, right)
		mid := (left + right) / 2
		need, cur := 1, 0
		for _, w := range weights {
			if cur+w > mid {
				need++
				cur = 0
			}
			cur += w
		}
		if need <= D {
			right = mid
		} else {
			left = mid + 1
		}
	}
	return left
}

func Max(weights []int) int {
	num := 0
	for _, w := range weights {
		if w > num {
			num = w
		}
	}
	return num
}

func Sum(nums []int) int {
	res := 0
	for _, num := range nums {
		res += num
	}
	return res
}

func main() {
	shipWithinDays([]int{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}, 5)
}
