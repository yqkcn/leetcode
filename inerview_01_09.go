package main

func isFlipedString(s1 string, s2 string) bool {
	if len(s1) != len(s2) {
		return false
	}
	if len(s1) == 0 {
		return true
	}
	for i := 0; i < len(s1); i++ {
		var str string
		if i == 0 {
			str = s1[1:] + string(s1[0])
		} else if i == len(s1)-1 {
			str = string(s1[len(s1)-1]) + s1[:len(s1)-1]
		} else {
			str = s1[i:] + s1[:i]
		}
		if str == s2 {
			return true
		}
	}
	return false
}
