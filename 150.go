package main

import (
	"fmt"
	"strconv"
)

func evalRPN(tokens []string) int {
	var nums []int
	for _, str := range tokens {
		len := len(nums)
		if str == "+" {
			num := nums[len-2] + nums[len-1]
			nums = nums[0 : len-2]
			nums = append(nums, num)
			continue
		}
		if str == "-" {
			num := nums[len-2] - nums[len-1]
			nums = nums[0 : len-2]
			nums = append(nums, num)
			continue
		}
		if str == "*" {
			num := nums[len-2] * nums[len-1]
			nums = nums[0 : len-2]
			nums = append(nums, num)
			continue
		}
		if str == "/" {
			num := nums[len-2] / nums[len-1]
			nums = nums[0 : len-2]
			nums = append(nums, num)
			continue
		}
		num, _ := strconv.Atoi(str)
		nums = append(nums, num)
	}
	return nums[0]
}

func main() {
	fmt.Print(evalRPN([]string{"4", "13", "5", "/", "+"}))
	fmt.Print(evalRPN([]string{"10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"}))
}
