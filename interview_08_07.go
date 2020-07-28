package main

func permutation(S string) []string {
	var res []string
	if len(S) < 2 {
		res = append(res, S)
		return res
	}
	// 挨个取字母作为第一个字母
	for i, str := range S {
		newS := S[:i]
		if i != len(S)-1 {
			newS += S[i+1:]
		}
		for _, s := range permutation(newS) {
			res = append(res, string(str)+s)
		}
	}
	return res
}
