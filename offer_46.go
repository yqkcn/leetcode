package main

import (
	"fmt"
	"strconv"
)

func main() {
	fmt.Print(translateNum(12258))
}

func translateNum(num int) int {
	s := strconv.Itoa(num)
	if len(s) == 1 {
		return 1
	}
	if len(s) == 2 {
		if num > 25 {
			return 1
		}
		return 2
	}
	num_1 := 1
	num_2 := 1
	i, _ := strconv.Atoi(s[:2])
	if i <= 25 {
		num_2 = 2
	}
	for i:=2;i<len(s);i++{
		j, _ := strconv.Atoi(s[i-1:i+1])
		if s[i-1] != '0' && j <= 25{
			num_1, num_2 = num_2, num_1 + num_2
		} else {
			num_1, num_2 = num_2, num_2
		}
	}
	return num_2

}
