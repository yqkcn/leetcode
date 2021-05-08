package main

func isPossible(nums []int) bool {
	counter := make(map[int]int)
	need := make(map[int]int)
	for _, num := range nums {
		counter[num]++
	}
	for _, num := range nums {
		if counter[num] == 0 {
			continue
		} else if need[num] > 0 {
			need[num]--
			counter[num]--
			need[num+1]++
		} else if counter[num] > 0 && counter[num+1] > 0 && counter[num+2] > 0 {
			counter[num]--
			counter[num+1]--
			counter[num+2]--
			need[num+3]++
		} else {
			return false
		}
	}
	return true
}
