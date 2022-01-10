package main

import "fmt"

func maxScoreSightseeingPair(values []int) int {
	// 构造两个数组，arr1 为正向 values[i] + i 最大值， arr2 位反向 values[j] - j 最大值
	var arr1, arr2 []int
	// 正向
	max_num := 0
	for i, num := range values {
		max_num = Max(max_num, i+num)
		arr1 = append(arr1, max_num)
	}
	// 反向
	max_num = -100000
	for i := len(values) - 1; i >= 0; i-- {
		max_num = Max(max_num, values[i]-i)
		arr2 = append(arr2, max_num)
	}
	arr2 = reverse(arr2)
	fmt.Printf("%v", arr1)
	fmt.Printf("%v", arr2)
	// 遍历
	ans := -1000000
	for i := 0; i < len(values)-1; i++ {
		ans = Max(ans, arr1[i] + arr2[i+1])
	}
	return ans
}

func Max(a, b int) int {
	if a >= b {
		return a
	} else {
		return b
	}
}

func reverse(numbers []int) []int {
	for i := 0; i < len(numbers)/2; i++ {
		j := len(numbers) - i - 1
		numbers[i], numbers[j] = numbers[j], numbers[i]
	}
	return numbers
}


func main() {

}
