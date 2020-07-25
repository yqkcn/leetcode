package main

func isAnagram(s string, t string) bool {
	if len(s) != len(t) {
		return false
	}
	count1, count2 := make(map[int32]int), make(map[int32]int)
	for _, str := range s {
		count1[str]++
	}
	for _, str := range t {
		count2[str]++
	}
	for k, v := range count1 {
		num2, ok := count2[k]
		if !ok || num2 != v {
			return false
		}
	}
	for k, v := range count2 {
		num1, ok := count1[k]
		if !ok || num1 != v {
			return false
		}
	}
	return true
}