package main

import (
	"fmt"
	"strconv"
)

func movingCount(m int, n int, k int) int {
	if m == 0 || n == 0 {
		return 0
	}
	if k == 0 {
		return 1
	}
	visited := make(map[[2]int]bool)
	visited[[2]int{0, 0}] = true
	cache := make(map[[2]int]bool)
	res := 0
	queue := [][2]int{{0, 1}, {1, 0}}
	for len(queue) != 0 {
		cur := queue[len(queue)-1]
		queue = queue[:len(queue)-1]
		if cache[cur] {
			continue
		}
		cache[cur] = true
		// 判断是否有效
		if cur[0] < 0 || cur[0] >= m || cur[1] < 0 || cur[1] >= n {
			continue
		}
		if isValid1(cur[0], cur[1], k) {
			a := [2]int{cur[0] - 1, cur[1]}
			b := [2]int{cur[0], cur[1] - 1}
			c := [2]int{cur[0], cur[1] + 1}
			d := [2]int{cur[0] + 1, cur[1]}
			if visited[a] || visited[b] || visited[c] || visited[d] {
				visited[cur] = true
				res += 1
				// 加入邻居
				if !cache[a] {
					queue = append(queue, a)
				}
				if !cache[b] {
					queue = append(queue, b)
				}
				if !cache[c] {
					queue = append(queue, c)
				}
				if !cache[d] {
					queue = append(queue, d)
				}
			}
		}
	}
	return res
}

func isValid1(m int, n int, k int) bool {
	num := strconv.FormatInt(int64(m), 10) + strconv.FormatInt(int64(n), 10)
	res := 0
	for _, str := range num {
		num, _ := strconv.Atoi(string(str))
		res += num
		if res > k {
			return false
		}
	}
	return true
}

func main() {
	fmt.Print(isValid1(35, 37, 18))
}
