package main

type NumArray struct {
	nums []int
}

func Constructor(nums []int) NumArray {
	return NumArray{nums: nums}
}

func (this *NumArray) Update(i int, val int) {
	this.nums[i] = val
}

func (this *NumArray) SumRange(i int, j int) int {
	res := 0
	for ; i <= j; i++ {
		res += this.nums[i]
	}
	return res
}

/**
 * Your NumArray object will be instantiated and called as such:
 * obj := Constructor(nums);
 * obj.Update(i,val);
 * param_2 := obj.SumRange(i,j);
 */
