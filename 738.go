package main

import (
	"strconv"
)

func monotoneIncreasingDigits(N int) int {
	if N < 10 {
		return N
	}
	cache := map[string]int{
		"0": 0,
		"1": 1,
		"2": 2,
		"3": 3,
		"4": 4,
		"5": 5,
		"6": 6,
		"7": 7,
		"8": 8,
		"9": 9,
	}
	s := strconv.Itoa(N)
	left := -1
	for i := 0; i < len(s)-1; i++ {
		if cache[string(s[i])] > cache[string(s[i+1])] {
			// 往前找相同的字母
			for j := 0; j <= i; j++ {
				if s[j] == s[i] {
					left = j
					break
				}
			}
			break
		}
	}
	if left == -1 {
		return N
	}
	var res string
	res += s[:left]
	res += strconv.Itoa(cache[string(s[left])] - 1)
	for i := left + 1; i < len(s); i++ {
		res += "9"
	}
	num, _ := strconv.Atoi(res)
	return num
}

func main() {
	monotoneIncreasingDigits(332)
}
