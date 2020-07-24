package main

func permutation(s string) []string {
	if len(s) == 0 {
		return []string{}
	}
	if len(s) == 1 {
		return []string{s}
	}
	return getAll("", s, make(map[string]bool))
}

func getAll(prefix string, s string, cache map[string]bool) []string {
	if cache[prefix] {
		return []string{}
	}
	cache[prefix] = true
	if len(s) == 1 {
		return []string{prefix + s}
	}
	var res []string
	for i := 0; i < len(s); i++ {
		var nextStr string
		if i == 0 {
			nextStr = s[1:]
		} else if i == len(s)-1 {
			nextStr = s[:len(s)-1]
		} else {
			nextStr = s[:i] + s[i+1:]
		}
		res = append(res, getAll(prefix+string(s[i]), nextStr, cache)...)
	}
	return res
}
