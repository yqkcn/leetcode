package main

func main() {
	combinationSum3(3, 7)
}

func combinationSum3(k int, n int) [][]int {
	var cur []int
	return combinationSum(k, n, 0, cur)
}

func combinationSum(k int, n int, curSum int, cur []int) [][]int {
	var res [][]int
	// 到最大长度，达到目标值返回，未达到返回空值
	if len(cur) == k {
		if curSum == n {
			res = append(res, cur)
		}
		return res
	}
	// 未到最大长度， 总和超过最大值，返回空
	if curSum >= n {
		return res
	}
	// 遍历大于 cur 最后一个元素的值，加入 cur
	target := 1
	if len(cur) != 0 {
		target = cur[len(cur)-1] + 1
	}
	for i := target; i <= 9; i++ {
		var newCur []int
		newCur = append(newCur, cur...)
		newCur = append(newCur, i)
		_tmp := combinationSum(k, n, curSum+i, newCur)
		if len(_tmp) != 0 {
			res = append(res, _tmp...)
		}
	}
	return res
}
