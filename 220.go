package main

func main() {
}

func containsNearbyAlmostDuplicate(nums []int, k int, t int) bool {
	if len(nums) == 0 {
		return false
	}
	for i, num := range nums[:len(nums)-1] {
		for j := i + 1; j < len(nums) && j < i+k+1; j++ {
			red := num - nums[j]
			if red < 0 {
				red *= -1
			}
			if red <= t {
				return true
			}
		}
	}
	return false
}
