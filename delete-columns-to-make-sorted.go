package main

func minDeletionSize(strs []string) int {
	if strs == nil || len(strs) == 1 {
		return 0
	}
	res := 0
	for i := 0; i < len(strs[0]); i++ {
		pre := strs[0][i]
		for _, str := range strs[1:] {
			if str[i] < pre {
				res++
				break
			} else {
				pre = str[i]
			}
		}
	}
	return res
}
