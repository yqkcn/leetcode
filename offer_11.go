package main

func minArray(numbers []int) int {
	if len(numbers) == 1 {
		return numbers[0]
	}
	res := numbers[0]
	for i := 0; i < len(numbers)-1; i++ {
		if numbers[i] > numbers[i+1] {
			res = numbers[i+1]
			break
		}
	}
	return res
}

