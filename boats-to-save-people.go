package main

import "sort"

func numRescueBoats(people []int, limit int) int {
	sort.Ints(people)
	num := 0
	for len(people) > 1 {
		num += 1
		num1, num2 := people[0], people[len(people)-1]
		// 可以放两个
		if num1+num2 <= limit {
			people = people[1 : len(people)-1]
		} else {
			// 放一个大的
			people = people[:len(people)-1]
		}
	}
	return num + len(people)
}