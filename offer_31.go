package main

func validateStackSequences(pushed []int, popped []int) bool {
	var stack []int
	idx := 0
	for _, num := range pushed {
		stack = append(stack, num)
		for len(stack) != 0 && popped[idx] == stack[len(stack)-1] {
			idx++
			stack = stack[:len(stack)-1]
		}

	}
	if idx == len(popped) {
		return true
	}
	return false
}

func main() {
	validateStackSequences([]int{1, 2, 3, 4, 5}, []int{4, 5, 3, 2, 1})
}
