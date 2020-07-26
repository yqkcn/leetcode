package main

import "fmt"

func numberToWords(num int) string {
	// 小于一千
	if num < 1000 {
		return getSimpleNumber(num)
	}
	// 小于一百万
	if num < 1000000 {
		a, b := num/1000, num%1000
		res := getSimpleNumber(a) + " Thousand"
		if b != 0 {
			res += " " + numberToWords(b)
		}
		return res

	}
	// 小于十亿
	if num < 1000000000 {
		a, b := num/1000000, num%1000000
		res := getSimpleNumber(a) + " Million"
		if b != 0 {
			res += " " + numberToWords(b)
		}
		return res
	}
	// 大于十亿
	a, b := num/1000000000, num%1000000000
	res := getSimpleNumber(a) + " Billion"
	if b != 0 {
		res += " " + numberToWords(b)
	}
	return res
}

func getSimpleNumber(n int) string {
	cache := map[int]string{
		0:  "Zero",
		1:  "One",
		2:  "Two",
		3:  "Three",
		4:  "Four",
		5:  "Five",
		6:  "Six",
		7:  "Seven",
		8:  "Eight",
		9:  "Nine",
		10: "Ten",
		11: "Eleven",
		12: "Twelve",
		13: "Thirteen",
		14: "Fourteen",
		15: "Fifteen",
		16: "Sixteen",
		17: "Seventeen",
		18: "Eighteen",
		19: "Nineteen",
		20: "Twenty",
		30: "Thirty",
		40: "Forty",
		50: "Fifty",
		60: "Sixty",
		70: "Seventy",
		80: "Eighty",
		90: "Ninety",
	}
	// 生成小于以前的数的字符串
	if n <= 20 {
		return cache[n]
	}
	// 两位
	if n < 100 {
		// 十位加个位
		a, b := n/10, n%10
		res := cache[a*10]
		if b != 0 {
			res += " " + cache[b]
		}
		return res
	}
	// 三位
	a, b := n/100, n%100
	res := cache[a] + " " + "Hundred"
	if b != 0 {
		res += " " + getSimpleNumber(b)
	}
	return res
}

func main() {
	fmt.Print(getSimpleNumber(0))
}
