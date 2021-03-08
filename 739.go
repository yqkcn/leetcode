package main

func dailyTemperatures(T []int) []int {
	var res []int
	if T == nil {
		return res
	}
	l := len(T)
	for i := 0; i < l; i ++ {
		num := 0
		for j := i + 1; j < l; j++ {
			if T[j] > T[i] {
				num = j - i
				break
			}
		}
		res = append(res, num)
	}
	return res
}
