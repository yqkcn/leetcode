package main

import "sort"

func numTriplets(nums1 []int, nums2 []int) int {
	sort.Ints(nums1)
	sort.Ints(nums2)
	sum := 0
	for _, num := range nums1 {
		cur := num * num
		for i := 0; i < len(nums2)-1; i++ {
			if nums2[i] > num {
				break
			}
			for j := i + 1; j < len(nums2); j++ {
				_num := nums2[i] * nums2[j]
				if _num > cur {
					break
				}
				if cur == _num {
					sum++
				}
			}
		}
	}
	for _, num := range nums2 {
		cur := num * num
		for i := 0; i < len(nums1)-1; i++ {
			if nums1[i] > num {
				break
			}
			for j := i + 1; j < len(nums1); j++ {
				_num := nums1[i] * nums1[j]
				if _num > cur {
					break
				}
				if cur == nums1[i]*nums1[j] {
					sum++
				}
			}
		}
	}
	return sum
}

func main() {
	numTriplets([]int{1, 3, 1, 2}, []int{2, 3, 5, 3, 2})
}
