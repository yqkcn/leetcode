package main

import "fmt"

func main() {
	fmt.Print(generateMatrix(3))
}

func generateMatrix(n int) [][]int {

	var res [][]int
	for i := 0; i < n; i ++ {
		res = append(res, make([]int, n))
	}

	if n == 0 {
		return res
	}

	min_r, max_r := 0, n - 1
	min_c, max_c := 0, n - 1
	r, c := 0, 0
	num := 0
	for num != n * n {
		fmt.Printf("%d\n", num)
		if r == min_r {
			if c == min_c {
				for i := c; i <= max_c; i++ {
					num += 1
					res[r][i] = num
				}
				r += 1
				c = max_c
				min_r += 1
			} else {
				for i := r; i <= max_r; i++ {
					num += 1
					res[i][c] = num
				}
				max_c -= 1
				c -= 1
				r = max_r
			}
			continue
		} else {
			if c == min_c {
				for i := r; i >= min_r; i-- {
					num += 1
					res[i][c] = num
				}
				c += 1
				min_c += 1
				r = min_r
			} else {
				for i := c; i >= min_c; i-- {
					num += 1
					res[r][i] = num
				}
				max_r -= 1
				r -= 1
				c = min_c
			}
		}
	}
	return res

}