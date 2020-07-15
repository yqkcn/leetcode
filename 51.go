package main

import (
	"fmt"
	"sort"
	"strconv"
	"strings"
)

func solveNQueens(n int) [][]string {
	if n == 0 {
		return [][]string{{}}
	}
	if n == 1 {
		return [][]string{{"Q"}}
	}
	var paths [][]string
	var points [][]int
	for i := 0; i < n; i++ {
		paths = append(paths, []string{})
		for j := 0; j < n; j++ {
			points = append(points, []int{i, j})
			paths[i] = append(paths[i], ".")
		}
	}
	var res [][]string
	for _, path := range getPoints(n, points, [][]int{}, make(map[string]bool)) {
		newPaths := copyPaths(paths)
		for _, point := range path {
			newPaths[point[0]][point[1]] = "Q"
		}
		var tmpPaths []string
		for _, p := range newPaths {
			tmpPaths = append(tmpPaths, strings.Join(p, ""))
		}
		res = append(res, tmpPaths)
	}
	return res
}

func getPoints(n int, points [][]int, take [][]int, cache map[string]bool) [][][]int {
	key := getKey(take)
	if cache[key] {
		return [][][]int{}
	}
	if n == 0 {
		cache[key] = true
		return [][][]int{take}
	}
	var res [][][]int
	// points 保存的是当前可用的
	for _, point := range points {
		newTake := copyPoints(take)
		newTake = append(newTake, point)
		var newPoints [][]int
		// 保存皇后以后，将能吃到的位置移除
		for _, newPoint := range points {
			if newPoint[0] == point[0] || newPoint[1] == point[1] || newPoint[0]-point[0] == newPoint[1]-point[1] || newPoint[0]-point[0]+newPoint[1]-point[1] == 0 {
				continue
			} else {
				newPoints = append(newPoints, newPoint)
			}
		}
		res = append(res, getPoints(n-1, newPoints, newTake, cache)...)
	}
	cache[key] = true
	return res
}

func getKey(take [][]int) string {
	sort.SliceStable(take, func(i, j int) bool {
		if take[i][0] < take[j][0] {
			return true
		}
		if take[i][0] > take[j][0] {
			return false
		}
		return take[i][1] < take[j][1]
	})
	key := ""
	for _, p := range take {
		key = key + ":" + strconv.Itoa(p[0]) + ":" + strconv.Itoa(p[1])
	}
	return key
}

func copyPoints(points [][]int) [][]int {
	var res [][]int
	for i := 0; i < len(points); i++ {
		res = append(res, []int{})
		for j := 0; j < len(points[i]); j++ {
			res[i] = append(res[i], points[i][j])
		}
	}
	return res
}

func copyPaths(paths [][]string) [][]string {
	var res [][]string
	for i := 0; i < len(paths); i++ {
		res = append(res, []string{})
		for j := 0; j < len(paths[i]); j++ {
			res[i] = append(res[i], paths[i][j])
		}
	}
	return res
}

func main() {
	fmt.Print(solveNQueens(9))
}
