package main

import (
	"fmt"
	"strconv"
	"strings"
)

func validUtf8(data []int) bool {
	if len(data) == 0 {
		return true
	}
	var strData []string
	for _, num := range data {
		str := strconv.FormatInt(int64(num), 2)
		if len(str) >= 8 {
			strData = append(strData, str[len(str)-8:])
		} else {
			n := 8 - len(str)
			for i := 0; i < n; i++ {
				str = "0" + str
			}
			strData = append(strData, str)
		}
	}
	fmt.Print(strData)
	start := 0
	for start < len(data) && len(strData) != 0 {
		cur := strData[start]
		if strings.HasPrefix(cur, "0") {
			start++
		} else if strings.HasPrefix(cur, "10") {
			return false
		} else if strings.HasPrefix(cur, "110") {
			// 两字节
			if start+1 >= len(strData) || !strings.HasPrefix(strData[start+1], "10") {
				return false
			}
			start += 2
		} else if strings.HasPrefix(cur, "1110") {
			// 3字节
			if start+2 >= len(strData) || !strings.HasPrefix(strData[start+1], "10") || !strings.HasPrefix(strData[start+2], "10") {
				return false
			}
			start += 3
		} else if strings.HasPrefix(cur, "11110") {
			// 4字节
			if start+3 >= len(strData) || !strings.HasPrefix(strData[start+1], "10") || !strings.HasPrefix(strData[start+2], "10") || !strings.HasPrefix(strData[start+3], "10") {
				return false
			}
			start += 4
		} else {
			return false
		}
	}
	return true
}

func main() {
	validUtf8([]int{235, 140, 4})
}