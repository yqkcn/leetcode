package main

func main() {
	rangeBitwiseAnd(5, 7)
}

func rangeBitwiseAnd(m int, n int) int {
	res := m
	for j := m + 1; j <= n; j ++ {
		res &= j
	}
	return res
}
