package main

func isSubsequence(s string, t string) bool {
	if len(s) == 0 {
		return true
	}
	if len(t) == 0 {
		return false
	}
	for i, _ := range t {
		if t[i] == s[0] {
			if len(s) == 1 {
				return true
			}
			if i == len(t)-1 {
				return false
			}
			return isSubsequence(s[1:], t[i+1:])
		}
	}
	return false
}
