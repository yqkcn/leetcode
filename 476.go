package main

import (
	"fmt"
	"strconv"
)

func findComplement(num int) int {
	xStr := strconv.FormatInt(int64(num), 2)
	var newStr string
	for _, str := range xStr {
		if str == '0' {
			newStr += "1"
		} else {
			newStr += "0"
		}
	}
	res, _ := strconv.ParseInt(newStr, 2, len(newStr))
	return int(res)
}

func main() {
	fmt.Print(findComplement(1))
}
