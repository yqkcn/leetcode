package main

func help(x float64, n int) float64 {
	if n == 1 {
		return x
	} else if n&1 == 0 {
		return help(x*x, n/2)
	} else {
		return x * help(x, n-1)
	}
}

func myPow(x float64, n int) float64 {
	if n < 0 {
		return help(1.0/x, -n)
	} else if n == 0 {
		return 1
	} else {
		return help(x, n)
	}
}