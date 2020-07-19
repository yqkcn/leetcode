package main

import (
	"strings"
)

func licenseKeyFormatting(S string, K int) string {
	S = strings.ToUpper(S)
	chars := strings.Split(S, "-")
	if len(chars) == 1 {
		return S
	}
	res := chars[0]
	newChars := strings.Join(chars[1:], "")
	if num := len(newChars) % K; num != 0 {
		if len(res)+num <= K {
			res += newChars[0:num]
			newChars = newChars[num:]
		} else {
			newChars = res[len(res)-K+num:] + newChars
			res = res[0 : len(res)-K+num]
		}
	}

	for i := 0; i < len(newChars); i += K {
		if i+K >= len(newChars) {
			res += "-" + newChars[i:]
			break
		}
		res += "-" + newChars[i:i+K]
	}
	return res
}

func main() {
	licenseKeyFormatting("2-4A0r7-4k", 4)
}
