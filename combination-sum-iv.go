package main

func combinationSum4(nums []int, target int) int {
	if target == 0 {
		return 0
	}
	dp := make([]int, target+1)
	dp[0] = 1
	for i := 1; i <= target; i++ {
		for _, num := range nums {
			if num > i {
				continue
			} else {
				dp[i] += dp[i-num]
			}
		}
	}
	return dp[target]
}

func main() {
	combinationSum4([]int{1, 2, 3}, 4)
}
