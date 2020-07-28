package main

func reverseVowels(s string) string {
	if len(s) < 2 {
		return s
	}
	newStr := []byte(s)
	cache := map[byte]bool{'a': true, 'e': true, 'i': true, 'o': true, 'u': true, 'A': true, 'E': true, 'I': true, 'O': true, 'U': true}
	left, right := 0, len(newStr)-1
	for left < right {
		if cache[newStr[left]] && cache[newStr[right]] {
			newStr[left], newStr[right] = newStr[right], newStr[left]
			left++
			right--
		} else if cache[newStr[left]] {
			right--
		} else if cache[newStr[right]] {
			left++
		} else {
			left++
			right--
		}
	}
	return string(newStr)
}
