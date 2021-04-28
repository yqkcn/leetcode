package main

func waysToChange(n int) int {
	res := 0
	visited := make(map[[4]int]bool)
	var dfs func([4]int, int)
	dfs = func(coins [4]int, cur int) {
		if _, ok := visited[coins]; ok {
			return
		}
		visited[coins] = true
		if cur == 0 {
			res++
			return
		}
		if cur < 0 {
			return
		}
		// 分别添加一个1分，5分，10分，25分
		coins[0]++
		dfs(coins, cur-1)
		coins[0]--
		coins[1]++
		dfs(coins, cur-5)
		coins[1]--
		coins[2]++
		dfs(coins, cur-10)
		coins[2]--
		coins[3]++
		dfs(coins, cur-25)
		coins[3]--
	}
	dfs([4]int{0, 0, 0, 0}, n)
	return res % 1000000007
}
