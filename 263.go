package main

func isUgly(num int) bool {
	if num == 0 {
		return false
	}
	if num == 1 {
		return true
	}
	ugly := []int{2, 3, 5}
	if find := Find(ugly, num); find {
		return true
	}
	if num % 2 !=0 && num % 3 !=0 && num % 5 !=0 {
		return false
	}
	for _, _num := range ugly {
		if num % _num == 0 {
			if !isUgly(num / _num) {
				return false
			}
		}
	}
	return true
}

func Find(nums []int, num int) bool {
	for _, _num := range nums {
		if num == _num {
			return true
		}
	}
	return false
}