package main

func canConstruct(ransomNote string, magazine string) bool {
	if len(ransomNote) > len(magazine) {
		return false
	}
	count1, count2 := make(map[int32]int), make(map[int32]int)
	for _, str := range ransomNote {
		count1[str]++
	}
	for _, str := range magazine {
		count2[str]++
	}
	for k, v := range count1 {
		num, ok := count2[k]
		if !ok || num < v {
			return false
		}
	}
	return true
}
