package main

func countGoodTriplets(arr []int, a int, b int, c int) int {
	res := 0
	for i := 0; i < len(arr)-2; i++ {
		for j := i + 1; j < len(arr)-1; j++ {
			for k := j + 1; k < len(arr); k++ {
				if Abs(arr[i]-arr[j]) <= a && Abs(arr[j]-arr[k]) <= b && Abs(arr[i]-arr[k]) <= c {
					res++
				}
			}
		}
	}
	return res
}

func Abs(x int) int {
	if x < 0 {
		return -x
	}
	return x
}
