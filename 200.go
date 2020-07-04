package main

import (
	"fmt"
	"strconv"
)

func numIslands(grid [][]byte) int {
	if len(grid) == 0 {
		return 0
	}
	m, n := len(grid), len(grid[0])
	marked := make(map[string]bool)
	num := 0
	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {
			key := strconv.Itoa(i) + strconv.Itoa(j)
			if _, ok := marked[key]; !ok{
				if grid[i][j] == []byte("0")[0] {
					marked[key] = true
					continue
				}
				num += 1
				labers := [][]int{{i, j}}
				for len(labers) != 0 {
					r, c := labers[0][0], labers[0][1]
					labers = labers[1:]
					if 0 <= r && r < m && 0 <= c && c < n {
						_key := strconv.Itoa(r) + strconv.Itoa(c)
						if _, ok := marked[_key]; !ok{
							marked[_key] = true
							if grid[r][c] == []byte("1")[0] {
								labers = append(labers, [][]int{{r, c - 1}, {r, c + 1}, {r - 1, c}, {r + 1, c}}...)
							}
						}
					}
				}
			}
		}
	}
	return num
}

func main() {
	param := [][]byte{
		{'1', '1', '1', '1', '0'},
		{'1', '1', '0', '1', '0'},
		{'1', '1', '0', '0', '0'},
		{'0', '0', '0', '0', '0'},
	}
	a := numIslands(param)
	fmt.Print(a)
	param2 := [][]byte{
		{'1', '1', '0', '0', '0'},
		{'1', '1', '0', '0', '0'},
		{'0', '0', '1', '0', '0'},
		{'0', '0', '0', '1', '1'},
	}
	fmt.Print(numIslands(param2))
}
