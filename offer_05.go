package main

import "strings"

func replaceSpace(s string) string {
	var res []string
	for _, str := range []byte(s) {
		if str != ' ' {
			res = append(res, string(str))
		} else {
			res = append(res, "%20")
		}
	}
	return strings.Join(res, "")
}
