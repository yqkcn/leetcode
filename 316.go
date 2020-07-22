package main

func removeDuplicateLetters(s string) string {
	points := make(map[int32]int)
	for i, str := range s {
		points[str] = i
	}
	var stack []int32
	set := make(map[int32]bool)
	for i, str := range s {
		// 不在栈中
		if !set[str] {
			// 删除栈顶比当前字符小，并且后续还会出现的字符
			for {
				_len := len(stack)
				if _len != 0 && stack[_len-1] > str && points[stack[_len-1]] > i {
					delete(set, stack[_len-1])
					stack = stack[:_len-1]
				} else {
					break
				}
			}
			stack = append(stack, str)
			set[str] = true
		}
	}
	res := ""
	for _, str := range stack {
		res += string(str)
	}
	return res
}
