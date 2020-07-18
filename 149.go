package main

import "fmt"

func maxPoints(points [][]int) int {
	// 空或者1个点或者两个点，肯定可以在一条直线上
	if len(points) < 3 {
		return len(points)
	}
	cache := make(map[[2]int]bool)
	maxNum := 0
	// 先假设不存在相同的点
	for i, point1 := range points[0: len(points)-1] {
		for _, point2 := range points[i+1: len(points)] {
			// 遍历数组所有的两点组合，确定斜率和截距
			// y = k * x + b
			// 垂直 x 轴
			if point1[0] == point2[0] {
				// 遍历数组，统计在直线上的点的个数
				num := 0
				for _, point := range points {
					if point[0] == point1[0]{
						num += 1
					}
				}
				// 更新最大值
				if num > maxNum {
					maxNum = num
				}
				continue
			}
			// 垂直 y 轴
			if point1[1] == point2[1] {
				// 遍历数组，统计在直线上的点的个数
				num := 0
				for _, point := range points {
					if point[1] == point1[1]{
						num += 1
					}
				}
				// 更新最大值
				if num > maxNum {
					maxNum = num
				}
				continue
			}
			// 正常直线，不一定会整数
			// 分数暂时搞懂，用四个数存
			k := (point1[1] - point2[1]) / (point1[0] - point2[0])
			b := point1[1] - k * point1[0]
			// 判断是否查找过
			if cache[[2]int{k, b}] {
				continue
			}
			cache[[2]int{k, b}] = true
			num := 0
			for _, point := range points {
				if point[1] == k * point[0] + b {
					num += 1
				}
			}
			// 更新最大值
			if num > maxNum {
				maxNum = num
			}
		}
	}
	fmt.Print(maxNum)
	return maxNum
}

func main() {
	maxPoints([][]int{{3,10},{0,2},{0,2},{3,10}})
}
