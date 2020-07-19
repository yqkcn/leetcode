package main

func nextGreaterElement(nums1 []int, nums2 []int) []int {
	cache := make(map[int]int)
	var res []int
	for _, num1 := range nums1 {
		if num, ok := cache[num1]; ok {
			res = append(res, num)
			continue
		}
		idx := -1
		for j, num2 := range nums2 {
			if num2 == num1 {
				idx = j
				break
			}
		}
		if idx == -1 || idx == len(nums2)-1 {
			res = append(res, -1)
			cache[num1] = -1
		} else {
			flag := false
			for _, num := range nums2[idx+1:] {
				if num > num1 {
					res = append(res, num)
					cache[num1] = num
					flag = true
					break
				}
			}
			if !flag {
				res = append(res, -1)
				cache[num1] = -1
			}
		}
	}
	return res
}
