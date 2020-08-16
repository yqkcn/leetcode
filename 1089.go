package main

func duplicateZeros(arr []int) {
	num := len(arr)
	for i := num - 1; i >= 0; i-- {
		if arr[i] == 0 {
			copy(arr[i+1:], arr[i:len(arr)-1])
		}
	}
}
