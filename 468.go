package main

import (
	"fmt"
	"strconv"
	"strings"
)

func validIPAddress(IP string) string {
	if isIP4(IP) {
		return "IPv4"
	}
	if isIP6(IP) {
		return "IPv6"
	}
	return "Neither"
}

func isIP4(s string) bool {
	if !strings.Contains(s, ".") {
		return false
	}
	strs := strings.Split(s, ".")
	if len(strs) != 4 {
		return false
	}
	for _, str := range strs {
		// 开头为0
		if len(str) == 0 {
			return false
		}
		if len(str) > 1 && strings.HasPrefix(str, "0") {
			return false
		}
		num, err := strconv.Atoi(str)
		if err != nil {
			return false
		}
		if num > 255 {
			return false
		}
	}
	return true
}

func isIP6(s string) bool {
	if !strings.Contains(s, ":") {
		return false
	}
	strs := strings.Split(s, ":")
	if len(strs) != 8 {
		return false
	}
	valid := "abcdefABCDEF0123456789"
	for _, str := range strs {
		if len(str) == 0 || len(str) > 4 {
			return false
		}
		for _, _s := range str {
			if !strings.Contains(valid, string(_s)) {
				return false
			}
		}
	}
	return true
}

func main() {
	fmt.Print(validIPAddress("20EE:FGb8:85a3:0:0:8A2E:0370:7334"))
}
