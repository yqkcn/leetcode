package main

func largeGroupPositions(s string) [][]int {
	var res [][]int
	if len(s) < 3 {
		return res
	}
	l, r := 0, 1
	for r < len(s) {
		if s[r] == s[l] {
			r++
			if r == len(s) && r-l > 2 {
				res = append(res, []int{l, r - 1})
			}
		} else {
			if r-l > 2 {
				res = append(res, []int{l, r - 1})
			}
			l, r = r, r+1
		}
	}
	return res
}

func main() {
	largeGroupPositions("abbxxxxzzy")
}
