package main

func getValidT9Words(num string, words []string) []string {
	dict := map[byte][]byte{
		'2': []byte{'a', 'b', 'c'},
		'3': []byte{'d', 'e', 'f'},
		'4': []byte{'g', 'h', 'i'},
		'5': []byte{'j', 'k', 'l'},
		'6': []byte{'m', 'n', 'o'},
		'7': []byte{'p', 'q', 'r', 's'},
		'8': []byte{'t', 'u', 'v'},
		'9': []byte{'w', 'x', 'y', 'z'},
	}
	var res []string
	for _, word := range words {
		if len(word) != len(num) {
			continue
		}
		// 判断 ok
		ok := true
		for i := 0; i < len(num); i++ {
			if !Contain(dict[num[i]], word[i]) {
				ok = false
				break
			}
		}
		if ok {
			res = append(res, word)
		}
	}
	return res
}

func Contain(slice []byte, val byte) bool {
	for _, item := range slice {
		if item == val {
			return true
		}
	}
	return false
}
