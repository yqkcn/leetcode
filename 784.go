package main

import "strings"

func letterCasePermutation(S string) []string {
	S =  strings.ToLower(S)
	res := []string{S}
	for i := range S {
		if S[i] >= 'a' {
			end := len(res)
			for  j:=0; j < end; j++{
				newTemp := []byte(res[j])
				newTemp[i] = S[i]-'a'+'A'
				res = append(res, string(newTemp))
			}
		}
	}

	return res
}
