package main

import (
	"strconv"
)

func hammingDistance(x int, y int) int {
	xStr := strconv.FormatInt(int64(x), 2)
	yStr := strconv.FormatInt(int64(y), 2)
	// 补全0
	if len(xStr) < len(yStr) {
		num := len(yStr) - len(xStr)
		for i := 0; i < num; i++ {
			xStr = "0" + xStr
		}
	} else {
		if len(xStr) > len(yStr) {
			num := len(xStr) - len(yStr)
			for i := 0; i < num; i++ {
				yStr = "0" + yStr
			}
		}
	}
	res := 0
	for i := 0; i < len(xStr); i++ {
		if xStr[i] != yStr[i] {
			res += 1
		}
	}
	return res
}

func main() {
	hammingDistance(1, 4)
}
