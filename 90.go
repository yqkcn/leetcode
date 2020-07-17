package main

func subsetsWithDup(nums []int) [][]int {
	var res [][]int
	if nums == nil {
		return res
	}
	// 计数
	count := make(map[int]int)
	for _, num := range nums {
		count[num]++
	}
	// 添加一个空数组
	res = append(res, []int{})
	cache := make(map[int]bool)
	// 按照原始顺序添加
	for _, num := range nums {
		if cache[num] {
			continue
		}
		var cur [][]int
		for i := 0; i < count[num]; i++ {

		}
	}

}
