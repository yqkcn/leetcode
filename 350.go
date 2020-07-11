package main

func intersect(nums1 []int, nums2 []int) []int {
	counter1 := getCounter(nums1)
	counter2 := getCounter(nums2)
	var res []int
	for num, count1 := range counter1 {
		count2, ok := counter2[num]
		if ok {
			for i := 0; i < count1 && i < count2; i++ {
				res = append(res, num)
			}
		}
	}
	return res
}

func getCounter(nums []int) map[int]int {
	res := make(map[int]int)
	for _, num := range nums {
		if _, ok := res[num]; ok {
			res[num] = res[num] + 1
		} else {
			res[num] = 1
		}
	}
	return res
}

func main() {
	intersect([]int{1, 2, 2, 2}, []int{2, 2})
}
