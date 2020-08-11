package main

import "strconv"

func subtractProductAndSum(n int) int {
	chars := []byte(strconv.Itoa(n))
	num1, num2 := 1, 0
	for _, char := range chars {
		num, _ := strconv.Atoi(string(char))
		num1 *= num
		num2 += num
	}
	return num1 - num2
}
