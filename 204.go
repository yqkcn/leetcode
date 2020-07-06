package main

import "fmt"

func main() {
	fmt.Print(countPrimes(10000))
}

func countPrimes(n int) int {
	count := 0
	signs := make([]bool, n)
	for i := 2; i < n; i++ {
		if signs[i] {
			continue
		}
		count++
		for j := 2 * i; j < n; j += i {
			signs[j] = true
		}
	}
	return count
}
