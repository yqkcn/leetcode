package main

func kidsWithCandies(candies []int, extraCandies int) []bool {
	var _max int
	for _, num := range candies {
		if num > _max {
			_max = num
		}
	}
	var res []bool
	for _, num := range candies {
		if num + extraCandies >= _max {
			res = append(res, true)
		} else {
			res = append(res, false)
		}
	}
	return res
}