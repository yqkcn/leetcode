package main

func maxCount(m int, n int, ops [][]int) int {
	if len(ops) == 0 {
		return m * n
	}
	r := ops[0][0]
	c := ops[0][1]
	for i := 1; i < len(ops); i++ {
		if r > ops[i][0] {
			r = ops[i][0]
		}
		if c > ops[i][1] {
			c = ops[i][1]
		}
	}
	return r * c
}
