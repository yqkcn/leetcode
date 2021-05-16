package main

import "strings"

func maxScore(s string) int {
	res := 0
	num0 := 0
	num1 := strings.Count(s, "1")
	for i, char := range s[:len(s)-1] {
		if i == 0 && char == '1' {
			num1--
		} else if char == '0' {
			num0++
		} else if char == '1' {
			num1--
		}
		if num0+num1 > res {
			res = num0 + num1
		}
	}
	return res
}
