package main

type MyQueue struct {
	values []int
}


/** Initialize your data structure here. */
func Constructor() MyQueue {
	return MyQueue{values: []int{}}
}


/** Push element x to the back of queue. */
func (this *MyQueue) Push(x int)  {
	this.values = append(this.values, x)
}


/** Removes the element from in front of queue and returns that element. */
func (this *MyQueue) Pop() int {
	tmp := this.values[0]
	this.values = this.values[1:]
	return tmp
}


/** Get the front element. */
func (this *MyQueue) Peek() int {
	return this.values[0]
}


/** Returns whether the queue is empty. */
func (this *MyQueue) Empty() bool {
	return len(this.values) == 0
}


/**
 * Your MyQueue object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Push(x);
 * param_2 := obj.Pop();
 * param_3 := obj.Peek();
 * param_4 := obj.Empty();
 */
