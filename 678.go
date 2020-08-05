package main

func checkValidString(s string) bool {
	return check(0, s)
}

func check(left int, s string) bool {
	if len(s) == 0 {
		return left == 0
	}
	for i, str := range s {
		if str == '(' {
			left++
		} else if str == ')' {
			if left == 0 {
				return false
			} else {
				left--
			}
		} else {
			if i == len(s)-1 {
				return left == 0 || left == 1
			}
			if left == 0 {
				return check(0, s[i+1:]) || check(1, s[i+1:])
			} else {
				return check(left, s[i+1:]) || check(left+1, s[i+1:]) || check(left-1, s[i+1:])
			}
		}
	}
	if left != 0 {
		return false
	}
	return true
}
