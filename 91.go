package main

import (
	"fmt"
	"strconv"
)

func numDecodings(s string) int {
	if s[0] == '0' {
		return 0
	}
	if len(s) == 1 {
		return 1
	}
	dq := []int{1}
	_num, _ := strconv.Atoi(s[:2])
	if _num <= 26 {
		if s[1] == '0' {
			dq = append(dq, 1)
		} else {
			dq = append(dq, 2)
		}

	} else {
		if s[1] == '0' {
			return 0
		} else {
			dq = append(dq, 1)
		}
	}
	if len(s) == 2 {
		return dq[1]
	}

	for i := 2; i < len(s); i++ {
		fmt.Printf("%v\n", dq)
		num, _ := strconv.Atoi(s[i-1 : i+1])
		if s[i] == '0' {
			if s[i-1] == '0' {
				return 0
			}
			if num > 26 {
				return 0
			}
			dq = append(dq, dq[i-2])
			continue
		}
		if s[i-1] == '0' {
			dq = append(dq, dq[i-1])
			continue
		}
		if num <= 26 {
			dq = append(dq, dq[i-1]+dq[i-2])
		} else {
			dq = append(dq, dq[i-1])
		}
	}
	return dq[len(dq)-1]
}

func main() {
	numDecodings("301")
}
