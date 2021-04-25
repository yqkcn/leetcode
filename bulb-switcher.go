package main

func bulbSwitch(n int) int {
	num := 0
	for i := 1; i*i <= n; i++ {
		num++
	}
	return num
}