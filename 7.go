func reverse(x int) int {
	var y int = 0
	for x != 0 {
		y = y*10 + x%10
		x = x / 10
	}
	if y > 2147483647 || y < -2147483648 {
		return 0
	}
	return y
}