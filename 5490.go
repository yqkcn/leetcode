package main

func minDays(n int) int {
	queue := [][2]int{{0, 0}, {1, 1}, {2, 2}, {3, 2}}
	for len(queue) != 0 {
		cur := queue[0]
		queue = queue[1:]
		if cur[0] == n {
			return cur[1]
		} else if cur[0] < n {
			if cur[0]+1 <= n {
				queue = append(queue, [2]int{cur[0] + 1, cur[1] + 1})
			}
			if cur[0]*2 <= n {
				queue = append(queue, [2]int{cur[0] * 2, cur[1] + 1})
			}
			if cur[0]*3 <= n {
				queue = append(queue, [2]int{cur[0] * 3, cur[1] + 1})
			}
		}
	}
	return 0
}
