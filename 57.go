package main

func insert(intervals [][]int, newInterval []int) [][]int {
	if newInterval == nil {
		return intervals
	}
	if intervals == nil {
		return [][]int{newInterval}
	}
	success := false
	var res [][]int
	for i, interval := range intervals {
		// 小于当前区间
		if newInterval[1] < interval[0] {
			res = append(res, newInterval)
			res = append(res, intervals[i:]...)
			success = true
			break
		}
		// 右端点在当前区间
		if newInterval[1] >= interval[0] && newInterval[1] <= interval[1] && newInterval[0] < interval[0] {
			// 修改新区间的右端点
			newInterval[1] = interval[1]
			continue
		}
		// 被当前区间包含
		if newInterval[0] >= interval[0] && newInterval[1] <= interval[1] {
			res = append(res, intervals[i:]...)
			success = true
			break
		}
		// 左端点在当前区间
		if newInterval[0] >= interval[0] && newInterval[0] <= interval[1] && newInterval[1] > interval[1] {
			// 修改新区间的左端点
			newInterval[0] = interval[0]
			continue
		}
		// 大于当前区间
		if newInterval[0] > interval[1] {
			res = append(res, interval)
			continue
		}
	}
	// success 为 false，没有添加成功，应添加到末尾
	if !success {
		res = append(res, newInterval)
	}
	return res
}
