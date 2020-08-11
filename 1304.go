package main

func sumZero(n int) []int {
	var res []int
	if n%2 == 0 {
		for i := 1; i <= n/2; i++ {
			res = append(res, i)
			res = append(res, -i)
		}
	} else {
		for i := 1; i <= n/2; i++ {
			res = append(res, i)
			res = append(res, -i)
		}
		res = append(res, 0)
	}
	return res
}
