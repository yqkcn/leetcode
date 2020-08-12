package main

import "strings"

func makeGood(s string) string {
	var stack []string
	for _, chr := range s {
		if len(stack) == 0 {
			stack = append(stack, string(chr))
		} else if chr >= 'a' && chr <= 'z' && stack[len(stack)-1] == strings.ToUpper(string(chr)) {
			stack = stack[:len(stack)-1]
		} else if chr >= 'A' && chr <= 'Z' && stack[len(stack)-1] == strings.ToLower(string(chr)) {
			stack = stack[:len(stack)-1]
		} else {
			stack = append(stack, string(chr))
		}
	}
	return strings.Join(stack, "")
}
