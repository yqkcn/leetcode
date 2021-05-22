package main


func trap(height []int) int {
	if len(height) < 2 {
		return 0
	}
	rains, maxIdx := []int{0}, 0
	for i := 1; i < len(height); i++ {
		// 比前一个矮， 不会多存雨水
		if height[i] <= height[i-1] {
			rains = append(rains, rains[i-1])
			continue
		}
		// 高于之前最高的，最高的到当前柱子之间雨水会增加
		if height[i] >= height[maxIdx] {
			rain := rains[maxIdx]
			for j := maxIdx + 1; j < i; j++ {
				rain += height[maxIdx] - height[j]
			}
			rains = append(rains, rain)
			maxIdx = i
			continue
		}
		// 低于之前最高的，往前找第一个高于当前柱子的
		rain := 0
		for j := i - 1; j >= maxIdx; j-- {
			if height[j] >= height[i] {
				rain += rains[j]
				break
			} else {
				rain += height[i] - height[j]
			}
		}
		rains = append(rains, rain)
	}
	return rains[len(rains)-1]
}
