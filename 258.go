package main

import "strconv"

func addDigits(num int) int {
	if 0 <= num && num <= 9{
		return num
	}
	_num := 0
	for _, s := range []byte(strconv.Itoa(num)) {
		_s, _ := strconv.Atoi(string(s))
		_num += _s
	}
	return addDigits(_num)
}
