package main

import "fmt"

func minOperations(n int) int {
	if n < 2 {
		return 0
	}
	res := 0
	// 奇数个
	if n%2 != 0 {
		for i := 0; 2*i+1 < n; i++ {
			res += n - 2*i - 1
		}
	} else if res%2 == 0 {
		// 偶数个
		for i := 0; i < n/2; i++ {
			res += n - 2*i - 1
		}
	}
	return res
}

func main() {
	fmt.Print(minOperations(6))
}
