package main

import (
	"fmt"
	"strings"
)

func fullJustify(words []string, maxWidth int) []string {
	var res []string
	var cur []string
	var curLength int
	for _, word := range words {
		// 刚好能够添加
		if curLength+len(cur)+len(word) == maxWidth {
			cur = append(cur, word)
			res = append(res, strings.Join(cur, " "))
			cur = []string{}
			curLength = 0
			continue
		}
		// 能够添加
		if curLength+len(cur)+len(word) < maxWidth {
			cur = append(cur, word)
			curLength += len(word)
			continue
		}
		// 添加不下
		if curLength+len(cur)+len(word) > maxWidth {
			// 只有一个元素
			if len(cur) == 1 {
				res = append(res, cur[0]+getJoiner(maxWidth-curLength))
				cur = []string{word}
				curLength = len(word)
				continue
			}
			spaceNumber := maxWidth - curLength
			joiner := getJoiner(spaceNumber / (len(cur) - 1))
			// 空格分布均匀，优先往左侧分
			leftFirst := spaceNumber % (len(cur) - 1)
			str := ""
			for j, w := range cur {
				str = str + w
				if j != len(cur)-1 {
					str += joiner
				}
				if leftFirst != 0 {
					str += " "
					leftFirst -= 1
				}
			}
			res = append(res, str)
			cur = []string{word}
			curLength = len(word)
			continue
		}
	}
	// 还有没有添加的
	if len(cur) != 0 {
		str := strings.Join(cur, " ") + getJoiner(maxWidth-curLength-len(cur)+1)
		res = append(res, str)
	}
	for _, ws := range res {
		fmt.Printf("%s:%d\n", ws, len(ws))
	}
	return res
}

func getJoiner(n int) string {
	res := ""
	for i := 0; i < n; i++ {
		res += " "
	}
	return res
}

func main() {
	fullJustify([]string{"This", "is", "an", "example", "of", "text", "justification."}, 16)
	fullJustify([]string{"What", "must", "be", "acknowledgment", "shall", "be"}, 16)
	fullJustify([]string{"Science", "is", "what", "we", "understand", "well", "enough", "to", "explain", "to", "a", "computer.", "Art", "is", "everything", "else", "we", "do"}, 20)
}
