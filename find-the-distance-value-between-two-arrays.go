package main

func findTheDistanceValue(arr1 []int, arr2 []int, d int) int {
	res := 0
	for _, num1 := range arr1 {
		cur := 1
		for _, num2 := range arr2 {
			if Abs(num1-num2) <= d {
				cur = 0
				break
			}
		}
		res += cur
	}
	return res
}

func Abs(x int) int {
	if x < 0 {
		return -x
	}
	return x
}