package main

import "fmt"

func hIndex1(citations []int) int {
	for i, num := range citations {
		if num >= len(citations)-i {
			return len(citations) - i
		}
	}
	return 0
}

func main() {
	fmt.Print(hIndex1([]int{1, 2}))
}
