package main

func modifyString(s string) string {
	if len(s) == 1 {
		if s != "?" {
			return s
		}
		return "a"
	}
	chars := []byte{'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'}
	stack := []byte{}
	for i, chr := range s {
		if chr != '?' {
			stack = append(stack, byte(chr))
		} else {
			if i == 0 {
				for _, _chr := range chars {
					if _chr != s[i+1] {
						stack = append(stack, _chr)
						break
					}
				}
			} else if i == len(s)-1 {
				for _, _chr := range chars {
					if _chr != stack[len(stack)-1] {
						stack = append(stack, _chr)
						break
					}
				}
			} else {
				for _, _chr := range chars {
					if _chr != stack[len(stack)-1] && _chr != s[i+1] {
						stack = append(stack, _chr)
						break
					}
				}
			}
		}
	}
	return string(stack)
}

func main() {
	modifyString("ubv?w")
}
