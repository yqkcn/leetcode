package main

import (
	"fmt"
	"sort"
	"strconv"
	"strings"
)

func minNumber(nums []int) string {
	if nums == nil {
		return ""
	}
	if len(nums) == 1 {
		return strconv.Itoa(nums[0])
	}
	var newNums []string
	for _, num := range nums {
		newNums = append(newNums, strconv.Itoa(num))
	}
	sort.Slice(newNums, func(i, j int) bool {
		return min(newNums[i], newNums[j])
	})
	return strings.Join(newNums, "")
}

func min(s1, s2 string) bool {
	return s1+s2 < s2+s1
}

func main() {
	fmt.Print(minNumber([]int{3, 30, 34, 5, 9}))
}
