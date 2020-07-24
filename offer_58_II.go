package main

func reverseLeftWords(s string, n int) string {
	if len(s) == 1 {
		return s
	}
	return s[n:] + s[:n]
}
