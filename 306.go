package main

import (
	"fmt"
	"strconv"
	"strings"
)

func isAdditiveNumber(num string) bool {
	// 找到前两个数即可
	for i := 1; i <= len(num)-2; i++ {
		if i > 1 && num[0] == '0' {
			return false
		}
		for j := i + 1; j <= len(num)-1; j++ {
			num1, _ := strconv.Atoi(num[:i])
			num2, _ := strconv.Atoi(num[i:j])
			if j-i > 1 && num[i] == '0' {
				break
			}
			fmt.Printf("%d:%d\n", num1, num2)
			if isValid(num1, num2, num[j:]) {
				return true
			}
		}
	}
	return false
}

func isValid(a int, b int, s string) bool {
	if len(s) != 1 && s[0] == '0' {
		return false
	}
	prefix := strconv.FormatInt(int64(a+b), 10)
	if !strings.HasPrefix(s, prefix) {
		return false
	}
	if len(s) == len(prefix) {
		return true
	}
	return isValid(b, a+b, s[len(prefix):])
}

func main() {
	isAdditiveNumber("1023")
}
