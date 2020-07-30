package main

import (
	"fmt"
	"strconv"
)

func convertToBase7(num int) string {
	if num == 0 {
		return "0"
	}
	flag := ""
	if num < 0 {
		num *= -1
		flag = "-"
	}
	cur := ""
	for num >= 7 {
		cur = strconv.Itoa(num%7) + cur
		num = num / 7
	}
	if num != 0 {
		cur = strconv.Itoa(num) + cur
	}
	return flag + cur
}

func main() {
	fmt.Print(convertToBase7(0))
}
