package main

func subsets(nums []int) [][]int {
	var res [][]int
	res = append(res, []int{})
	for _, num := range nums {
		var newRes [][]int
		newRes = append(newRes, res...)
		for _, item := range res {
			var newItem []int
			newItem = append(newItem, item...)
			newItem = append(newItem, num)
			newRes = append(newRes, newItem)
		}
		res = newRes
	}
	return res
}

func main() {
	subsets([]int{1, 2, 3})
}
