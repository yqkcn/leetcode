package main

import "strconv"

func convertTime(current string, correct string) int {
	res := 0
	hour1, _ := strconv.Atoi(current[:2])
	minute1, _ := strconv.Atoi(current[3:])
	hour2, _ := strconv.Atoi(correct[:2])
	minute2, _ := strconv.Atoi(correct[3:])
	res += hour2 - hour1
	// 在一步操作中，你可以将 current 这个时间增加 1、5、15 或 60 分钟
	minute := 0
	if minute1 > minute2 {
		res -= 1
		minute = minute2 + 60 - minute1
	} else if minute1 < minute2 {
		minute = minute2 - minute1
	}
	for minute > 0 {
		if minute >= 15 {
			res += minute / 15
			minute %= 15
		} else if minute >= 5 {
			res += minute / 5
			minute %= 5
		} else {
			res += minute
			minute = 0
		}
	}
	return res
}
