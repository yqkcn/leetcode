package main

import (
	"strconv"
	"strings"
)

func hammingWeight(num uint32) int {
	str := strconv.FormatUint(uint64(num), 2)
	return strings.Count(str, "1")
}
