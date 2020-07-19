package main

import "strings"

func findWords(words []string) []string {
	cache1, cache2, cache3 := make(map[string]bool), make(map[string]bool), make(map[string]bool)
	for _, str := range []string{"q", "w", "e", "r", "t", "y", "u", "i", "o", "p"} {
		cache1[str] = true
	}
	for _, str := range []string{"a", "s", "d", "f", "g", "h", "j", "k", "l"} {
		cache2[str] = true
	}
	for _, str := range []string{"z", "x", "c", "v", "b", "n", "m"} {
		cache3[str] = true
	}
	var res []string
	for _, word := range words {
		isValid := true
		lowerWord := strings.ToLower(word)
		// 三行
		var curCache map[string]bool
		if cache1[string(lowerWord[0])] {
			curCache = cache1
		} else {
			if cache2[string(lowerWord[0])] {
				curCache = cache2
			} else {
				curCache = cache3
			}
		}
		for _, char := range lowerWord {
			if !curCache[string(char)] {
				isValid = false
				break
			}
		}
		if isValid {
			res = append(res, word)
		}
	}
	return res
}
