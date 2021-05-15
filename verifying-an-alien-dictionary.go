package main

func isAlienSorted(words []string, order string) bool {
	if words == nil || len(words) == 1 {
		return true
	}
	index := make(map[rune]int)
	for i, char := range order {
		index[char] = i
	}
	for i := 0; i < len(words)-1; i++ {
		if !compareWord(words[i], words[i+1], index) {
			return false
		}
	}
	return true
}

func compareWord(w1, w2 string, index map[rune]int) bool {
	if w1 == w2 {
		return true
	}
	for i := 0; i < len(w1) && i < len(w2); i++ {
		if index[rune(w1[i])] < index[rune(w2[i])] {
			return true
		} else if index[rune(w1[i])] > index[rune(w2[i])] {
			return false
		}
	}
	return len(w1) < len(w2)
}
