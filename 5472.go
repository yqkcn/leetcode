package main

import "strings"

func restoreString(s string, indices []int) string {
	if len(s) < 2 {
		return s
	}
	res := make([]string, len(s))
	for i, str := range s {
		res[indices[i]] = string((str))
	}
	return strings.Join(res, "")
}
