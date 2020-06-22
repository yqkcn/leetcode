package main

func main() {
	params := []int{1,2,3,4}
	productExceptSelf(params)
}

func productExceptSelf(nums []int) []int {
	var res []int
	cache := make(map[int]int)
	for i, num := range nums {
		_, found := cache[num]
		if !found {
			var _nums []int
			_nums = append(_nums, nums[:i]...)
			_nums = append(_nums, nums[i+1:len(nums)]...)
			cache[num] = getMul(_nums)
		}
		res = append(res, cache[num])
	}
	return res
}

func getMul(nums []int) int {
	res := 1
	for _, num := range nums {
		res *= num
	}
	return res
}