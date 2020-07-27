package main

func oneEditAway(first string, second string) bool {
	if first == "" && second == "" {
		return true
	}
	res := 0
	if len(first) == len(second) {
		for i := 0; i < len(first); i++ {
			if first[i] != second[i] {
				res++
			}
		}
		if res < 2 {
			return true
		}
		return false
	}
	if len(second)-len(first) > 1 || len(first)-len(second) > 1 {
		return false
	}
	if len(first) < len(second) {
		first, second = second, first
	}
	// 1长2短
	for i := 0; i < len(second); i++ {
		if first[i] != second[i] {
			return first[i+1:] == second[i:]
		}
	}
	return true
}
