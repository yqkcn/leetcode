package main

import "strings"

func findOcurrences(text string, first string, second string) []string {
	chars := strings.Split(text, " ")
	if len(chars) < 3 {
		return []string{}
	}
	var res []string
	for i := 2; i < len(chars); i++ {
		if chars[i-2] == first && chars[i-1] == second {
			res = append(res, chars[i])
		}
	}
	return res
}
