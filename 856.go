package main

import (
	"strconv"
)

func scoreOfParentheses(S string) int {
	if len(S) == 0 {
		return 0
	}
	var stack []string
	for _, s := range S {
		if s == '(' {
			stack = append(stack, "(")
		} else {
			if stack[len(stack)-1] == "(" {
				stack[len(stack)-1] = "1"
				if len(stack) > 1 {
					num, err := strconv.Atoi(stack[len(stack)-2])
					if err == nil {
						stack[len(stack)-2] = strconv.Itoa(num + 1)
						stack = stack[:len(stack)-1]
					}
				}
			} else {
				num, _ := strconv.Atoi(stack[len(stack)-1])
				stack[len(stack)-2] = strconv.Itoa(num * 2)
				stack = stack[:len(stack)-1]
				if len(stack) > 1 {
					_num, err := strconv.Atoi(stack[len(stack)-2])
					if err == nil {
						stack[len(stack)-2] = strconv.Itoa(num*2 + _num)
						stack = stack[:len(stack)-1]
					}
				}
			}
		}
	}

	num, _ := strconv.Atoi(stack[0])
	return num
}

func main() {
	scoreOfParentheses("(()(()))")
}
