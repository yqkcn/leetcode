package main

//动态规划方法 Time: O(n), Space: O(n)
func nthUglyNumber(n int) int {
	if n <= 0 { // 非法输入
		return -1 // 返回-1
	}
	uglyNums := make([]int, n) // 定义丑数数组
	uglyNums[0] = 1            // 并且初始化第0个丑数为1
	p2, p3, p5 := 0, 0, 0      //定义三个游标，指向用于乘以2,3,5的丑数
	for i := 1; i < n; i++ {   // i从1开始遍历到n-1一个个计算丑数
		// 我们用p2,p3,p5指向的丑数,分别去乘以2,3,5,然后去计算这3个数字的最小值
		m := min(uglyNums[p2]*2, uglyNums[p3]*3, uglyNums[p5]*5)
		// 这个最小值就是第i个丑数
		uglyNums[i] = m
		// 接着把等于最小值丑数的候选者游标+1,这样才能产生更大的候选丑数
		if m == uglyNums[p2]*2 { p2++ }
		if m == uglyNums[p3]*3 { p3++ }
		if m == uglyNums[p5]*5 { p5++ }
	}
	// 循环结束后返回下标为n-1的值即可
	return uglyNums[n-1]
}

// 辅助函数 求三个整数的最小值
func min(a, b, c int) int {
	return minm(a, minm(b, c))
}

func minm(a, b int) int {
	if a < b {
		return a
	}
	return b
}
