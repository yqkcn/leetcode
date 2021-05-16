package main

func destCity(paths [][]string) string {
	visited := make(map[string]bool)
	for _, path := range paths {
		visited[path[0]] = true
	}
	var res string
	for _, path := range paths {
		if !visited[path[1]] {
			res = path[1]
			break
		}
	}
	return res
}
