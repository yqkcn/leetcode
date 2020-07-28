package main

func palindromePairs(words []string) [][]int {
	var res [][]int
	if len(words) < 2 {
		return res
	}
	cache := make(map[string]bool)
	for i := 0; i < len(words)-1; i++ {
		for j := i + 1; j < len(words); j++ {
			str1 := words[i] + words[j]
			is, ok := cache[str1]
			if !ok {
				if isPalindrome(str1) {
					res = append(res, []int{i, j})
					cache[str1] = true
				} else {
					cache[str1] = false
				}
			} else if is {
				res = append(res, []int{i, j})
			}

			str2 := words[j] + words[i]
			is, ok = cache[str2]
			if !ok {
				if isPalindrome(str2) {
					res = append(res, []int{j, i})
					cache[str2] = true
				} else {
					cache[str2] = false
				}
			} else if is {
				res = append(res, []int{j, i})
			}
		}
	}
	return res
}

func isPalindrome(s string) bool {
	left, right := 0, len(s)-1
	for left < right {
		if s[left] != s[right] {
			return false
		} else {
			left++
			right--
		}
	}
	return true
}
