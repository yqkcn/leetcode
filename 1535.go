package main

import (
	"fmt"
	"sort"
)

func getWinner(arr []int, k int) int {
	if k >= len(arr) {
		sort.Ints(arr)
		return arr[len(arr)-1]
	}
	num := 0
	for num < k {
		fmt.Printf("%v:%d\n", arr, num)
		all := true
		i := 1
		for ; i <= k-num; i++ {
			if arr[0] < arr[i] {
				all = false
				break
			}
		}
		if all {
			return arr[0]
		}
		num = 1
		var newArr []int
		newArr = append(newArr, arr[i:]...)
		for j := 1; j < i; j++ {
			newArr = append(newArr, arr[i])
		}
		newArr = append(newArr, arr[0])
		arr = newArr
	}
	return arr[0]
}

func main() {
	getWinner([]int{2, 1, 3, 5, 4, 6, 7}, 2)
}
