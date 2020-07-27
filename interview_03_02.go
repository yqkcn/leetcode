package main

type MinStack struct {
	values    []int
	minValues []int
}

/** initialize your data structure here. */
func Constructor() MinStack {
	return MinStack{values: []int{}, minValues: []int{}}
}

func (this *MinStack) Push(x int) {
	// 添加元素
	this.values = append(this.values, x)
	// 添加最小元素
	if len(this.minValues) != 0 && x > this.minValues[len(this.minValues)-1] {
		this.minValues = append(this.minValues, this.minValues[len(this.minValues)-1])
	} else {
		this.minValues = append(this.minValues, x)
	}
}

func (this *MinStack) Pop() {
	this.values = this.values[:len(this.values)-1]
	this.minValues = this.minValues[:len(this.minValues)-1]
}

func (this *MinStack) Top() int {
	return this.values[len(this.values)-1]
}

func (this *MinStack) Min() int {
	return this.minValues[len(this.minValues)-1]
}

/**
 * Your MinStack object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Push(x);
 * obj.Pop();
 * param_3 := obj.Top();
 * param_4 := obj.Min();
 */
