package main

func canCompleteCircuit(gas []int, cost []int) int {
	length := len(gas)
	for i := 0; i < length; i++ {
		// 从节点 i 出发
		// 到不了下一个节点
		if gas[i] < cost[i] {
			continue
		}
		start := i
		cur := 0
		for j := 0; j < length; j++ {
			cur += gas[start%length]
			if cur < cost[start%length] {
				break
			}
			cur -= cost[start%length]
			start++
		}
		if start%length == i {
			return i
		}
	}
	return -1
}
