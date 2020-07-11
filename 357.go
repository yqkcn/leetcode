package main

func countNumbersWithUniqueDigits(n int) int {
	res := 0
	for i := 0; i <= n; i++ {
		res += get(i)
	}
	return res
}

func get(n int) int {
	if n == 0 {
		return 1
	}
	if n == 1 {
		return 9
	}
	res := 0
	num := 9
	for i := 0; i < n-1; i++ {
		num *= 9 - i
	}
	return res + num
}

func main() {
	countNumbersWithUniqueDigits(3)
}
