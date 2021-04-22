package main

func reverseStr(s string, k int) string {
	var res string
	length := len(s)
	for idx := 0; idx < length; idx += 2 * k {
		if idx+k >= length {
			res += Reverse(s[idx:])
		} else {
			res += Reverse(s[idx : idx+k])
			if idx+2*k >= length {
				res += s[idx+k:]
			} else {
				res += s[idx+k : idx+2*k]
			}
		}
	}
	return res
}

func Reverse(s string) (result string) {
	for _, v := range s {
		result = string(v) + result
	}
	return
}
