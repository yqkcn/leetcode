package main

func constructArr(a []int) []int {
	if len(a) == 0 {
		return []int{}
	}
	if len(a) == 1 {
		return []int{0}
	}
	cache := make(map[int]int)
	var res []int
	for i, num := range a {
		if mul, ok := cache[num]; ok {
			res = append(res, mul)
		} else {
			var mul int
			if i == 0 {
				mul = getM(a[1:])
			} else if i == len(a)-1 {
				mul = getM(a[:len(a)-1])
			} else {
				mul = getM(a[:i]) * getM(a[i+1:])
			}
			res = append(res, mul)
			cache[num] = mul
		}
	}
	return res
}

func getM(nums []int) int {
	res := 1
	for _, num := range nums {
		res *= num
	}
	return res
}
