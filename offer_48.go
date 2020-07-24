package main

func lengthOfLongestSubstring(s string) int {
	if len(s) < 2 {
		return len(s)
	}
	res, left, right := 1, 0, 1
	cache := make(map[uint8]bool)
	cache[s[0]] = true
	for right < len(s) {
		// 当前字符已经存在
		if cache[s[right]] {
			// 删除最左侧字符
			delete(cache, s[left])
			left++
			continue
		} else {
			// 不包含，右移
			cache[s[right]] = true
			right++
			if right-left > res {
				res = right - left
			}
		}
	}
	return res
}
