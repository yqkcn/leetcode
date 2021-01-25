package main

import "fmt"

func addToArrayForm(A []int, K int) []int {
	num := 0
	for l := len(A) - 1; l >= 0; l-- {
		cur := A[l] + num + K%10
		if cur < 10 {
			A[l] = cur
			num = 0
		} else {
			cur -= 10
			num = 1
			A[l] = cur
		}
		K /= 10
	}
	K += num
	for K != 0 {
		A = append([]int{K % 10}, A...)
		K /= 10
	}
	fmt.Print(A)
	return A
}

func main() {
	addToArrayForm([]int{1, 2, 0, 0}, 34)
}
