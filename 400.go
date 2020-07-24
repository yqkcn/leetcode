package main

import (
	"fmt"
	"math"
	"strconv"
)

func findNthDigit(n int) int {
	if n < 10 {
		return n
	}
	n -= 10
	i := 2
	for {
		num := 9 * i * int(math.Pow10(i-1))
		if n <= num {
			break
		} else {
			n -= num
			i++
		}
	}
	// 第几个数
	x, y := n/i, n%i
	num := int(math.Pow10(i-1)) + x
	numStr := strconv.Itoa(num)
	res, _ := strconv.Atoi(string(numStr[y]))
	return res
}

func main() {
	fmt.Print(findNthDigit(13))
}
