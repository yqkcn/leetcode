package main

import (
	"fmt"
	"strconv"
)

func summaryRanges(nums []int) []string {
	var res []string
	if len(nums) == 0 {
		return res
	}
	if len(nums) == 1 {
		return []string{strconv.Itoa(nums[0])}
	}
	first, second := 0, 1
	for second < len(nums) {
		if second == len(nums) - 1 {
			if nums[second] == nums[second-1] + 1 {
				res = append(res, strconv.Itoa(nums[first]) + "->" + strconv.Itoa(nums[second]))
			} else if second - first == 1 {
				// 只有一个元素，添加单个
				res = append(res, strconv.Itoa(nums[first]))
				res = append(res, strconv.Itoa(nums[second]))
			} else {
				res = append(res, strconv.Itoa(nums[first]) + "->" + strconv.Itoa(nums[second-1]))
				res = append(res, strconv.Itoa(nums[second]))
			}
			break
		}

		// 区间连续，继续添加
		if nums[second] == nums[second-1] + 1 {
			second++
			continue
		}
		// 不连续，添加区间
		if second - first == 1 {
			// 只有一个元素，添加单个
			res = append(res, strconv.Itoa(nums[first]))
		} else {
			res = append(res, strconv.Itoa(nums[first]) + "->" + strconv.Itoa(nums[second-1]))
		}
		first, second = second, second + 1
	}
	return res
}
func main() {
	fmt.Print(summaryRanges([]int{0,2,3,4,5,8,9,10}))
}
