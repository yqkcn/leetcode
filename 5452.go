package main

import "sort"

//给你一个数字数组 arr 。
//如果一个数列中，任意相邻两项的差总等于同一个常数，那么这个数列就称为 等差数列 。
//如果可以重新排列数组形成等差数列，请返回 true ；否则，返回 false

func canMakeArithmeticProgression(arr []int) bool {
	sort.Ints(arr)
	target := arr[1] - arr[0]
	for i := 0; i < len(arr)-1; i++ {
		if arr[i+1] - arr[i] != target {
			return false
		}
	}
	return true
}
