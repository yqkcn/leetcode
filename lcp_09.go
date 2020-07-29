package main

func minJump(jump []int) int {
	if len(jump) == 0 {
		return 0
	}
	target := len(jump)
	visited := map[int]bool{0: true}
	queue := [][2]int{{0, jump[0]}}
	for len(queue) != 0 {
		// 取出第一个元素
		cur := queue[0]
		queue = queue[1:]
		// 能够跳出
		if cur[0]+jump[cur[0]] > target {
			return cur[1]
		}
		// 不能跳出，将能够达到的添加到队列
		// 右侧
		if !visited[cur[0]+jump[cur[0]]] {
			queue = append(queue, [2]int{cur[0] + jump[cur[0]], cur[1] + 1})
			visited[cur[0]+jump[cur[0]]] = true
		}
		// 左侧所有
		for i := 0; i < cur[0]; i++ {
			if !visited[i] {
				queue = append(queue, [2]int{i, cur[1] + 1})
				visited[i] = true
			}
		}
	}

	return 0
}
