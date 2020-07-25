package main

import "strconv"

func getHint(secret string, guess string) string {
	a, b := 0, 0
	count1, count2 := make(map[uint8]int), make(map[uint8]int)
	for i:=0;i<len(secret);i++{
		if secret[i] == guess[i] {
			a++
		} else {
			count1[secret[i]]++
			count2[guess[i]]++
		}
	}
	for k, v := range count2 {
		num , ok := count1[k]
		if ok {
			b += min(num, v)
		}
	}
	return strconv.Itoa(a) + "A" + strconv.Itoa(b) + "B"
}

func min(a,b int) int {
	if a < b{
		return a
	}
	return b
}
