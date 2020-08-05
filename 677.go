package main

import "strings"

type MapSum struct {
	cache map[string]int
}

/** Initialize your data structure here. */
func Constructor() MapSum {
	return MapSum{cache: make(map[string]int)}
}

func (this *MapSum) Insert(key string, val int) {
	this.cache[key] = val
}

func (this *MapSum) Sum(prefix string) int {
	res := 0
	for k, v := range this.cache {
		if strings.HasPrefix(k, prefix) {
			res += v
		}
	}
	return res
}

/**
 * Your MapSum object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Insert(key,val);
 * param_2 := obj.Sum(prefix);
 */
