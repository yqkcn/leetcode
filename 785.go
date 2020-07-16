package main

import "fmt"

func isBipartite(graph [][]int) bool {
	if graph == nil {
		return true
	}
	if len(graph) == 1 {
		return true
	}
	setA, setB := make(map[int]bool), make(map[int]bool)
	return isValid(graph, setA, setB)
}

func isValid(graph [][]int, setA map[int]bool, setB map[int]bool) bool {
	res := true
	for i, vertexes := range graph {
		// 在 A，判断边的另一个顶点是否也在 A
		if setA[i] {
			for _, vertex := range vertexes {
				if setA[vertex] {
					return false
				} else {
					setB[vertex] = true
				}
			}
			continue
		}
		// 在 B， 判断边的另一个顶点是否也在 B
		if setB[i] {
			for _, vertex := range vertexes {
				if setB[vertex] {
					return false
				} else {
					setA[vertex] = true
				}
			}
			continue
		}
		// 都不在,第一次碰到，放进 A 或者 B
		newSetA := copyMap(setA)
		newSetA[i] = true
		newSetB := copyMap(setB)
		newSetB[i] = true
		res = isValid(graph, newSetA, copyMap(setB)) || isValid(graph, copyMap(setA), newSetB)
		break
	}
	fmt.Print(res)
	return res
}

func copyMap(setA map[int]bool) map[int]bool {
	newSetA := make(map[int]bool)
	for k, v := range setA {
		newSetA[k] = v
	}
	return newSetA
}

func main() {
	isBipartite([][]int{{1}, {0, 3}, {3}, {1, 2}})
}
