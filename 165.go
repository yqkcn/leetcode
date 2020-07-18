package main

import (
	"fmt"
	"strconv"
	"strings"
)

func compareVersion(version1 string, version2 string) int {
	strs1 := strings.Split(version1, ".")
	strs2 := strings.Split(version2, ".")
	// 补全0
	if len(strs1) < len(strs2) {
		num := len(strs2) - len(strs1)
		for i := 0; i < num; i++ {
			strs1 = append(strs1, "0")
		}
	} else {
		if len(strs1) > len(strs2) {
			num := len(strs1) - len(strs2)
			for i := 0; i < num; i++ {
				fmt.Print(i)
				fmt.Print(strs2)
				strs2 = append(strs2, "0")
			}
		}
	}
	for i := 0; i < len(strs1); i++ {
		num1, _ := strconv.Atoi(strs1[i])
		num2, _ := strconv.Atoi(strs2[i])
		if num1 == num2 {
			continue
		}
		if num1 < num2 {
			return -1
		}
		if num1 > num2 {
			return 1
		}
	}
	return 0
}

func main() {
	fmt.Print(compareVersion("1.0.1", "1"))
}
