package main

import "fmt"

func isPerfectSquare(num int) bool {
	if num == 0 || num == 1 {
		return true
	}
	m, n := 1, num/2
	for m < n {
		if m+1 == n {
			return m*m == num || n*n == num
		}
		mid := (m + n) / 2
		if mid*mid == num {
			return true
		}
		if mid*mid < num {
			m = mid
			continue
		}
		n = mid

	}
	return false
}

func main() {
	fmt.Print(isPerfectSquare(14))
}
