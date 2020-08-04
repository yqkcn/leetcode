package main

import (
	"strconv"
	"strings"
)

func decodeString(s string) string {
	var stack []string
	for _, str := range s {
		if str != ']' {
			if IsNum(string(str)) && len(stack) != 0 && IsNum(stack[len(stack)-1]) {
				stack[len(stack)-1] += string(str)
			} else {
				stack = append(stack, string(str))
			}
		} else {
			// 出栈，找到左括号和数字
			var cur string
			var num int
			for len(stack) != 0 {
				top := stack[len(stack)-1]
				stack = stack[:len(stack)-1]
				if top == "[" {
					num, _ = strconv.Atoi(stack[len(stack)-1])
					stack = stack[:len(stack)-1]
					break
				} else {
					cur = top + cur
				}
			}
			var _s string
			for i := 0; i < num; i++ {
				_s += cur
			}
			stack = append(stack, _s)
		}
	}
	return strings.Join(stack, "")
}
func IsNum(s string) bool {
	_, err := strconv.ParseFloat(s, 64)
	return err == nil
}
