package main

func firstUniqChar(s string) byte {
	count := make(map[int32]int)
	for _, str := range s {
		count[str]++
	}
	for _, str := range s {
		if count[str] == 1 {
			return byte(str)
		}
	}
	return ' '
}
