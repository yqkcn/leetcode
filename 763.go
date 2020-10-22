package main

func partitionLabels(S string) []int {
	if len(S) == 0 {
		return []int{}
	}
	idx := make(map[string]int)
	// 统计最后一次出现的位置
	for i, s := range S {
		idx[string(s)] = i
	}
	var res []int
	l, r := 0, idx[string(S[0])]
	start := l
	// 遍历
	for l < len(S) {
		if l == r {
			res = append(res, r-start+1)
			// 设置 left 和 right
			if l == len(S)-1 {
				break
			}
			l++
			start = l
			r = idx[string(S[l])]
			continue
		}
		if idx[string(S[l])] > r {
			r = idx[string(S[l])]
		}
		l++
	}
	return res
}

func main() {
	partitionLabels("ababcbacadefegdehijhklij")
}
