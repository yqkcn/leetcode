package main

type RecentCounter struct {
	values []int
}

func Constructor() RecentCounter {
	return RecentCounter{values: []int{}}
}

func (this *RecentCounter) Ping(t int) int {
	this.values = append(this.values, t)
	left := t - 3000
	res := 0
	for _, value := range this.values {
		if left <= value && value <= t {
			res++
		}
	}
	return res
}

/**
 * Your RecentCounter object will be instantiated and called as such:
 * obj := Constructor();
 * param_1 := obj.Ping(t);
 */
