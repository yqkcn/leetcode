package main

func isPowerOfFour(num int) bool {
	for i := 1; i <= num; i *= 4 {
		if i == num {
			return true
		}
	}
	return false
}
