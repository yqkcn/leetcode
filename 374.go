package main

/**
 * Forward declaration of guess API.
 * @param  num   your guess
 * @return 	     -1 if num is lower than the guess number
 *			      1 if num is higher than the guess number
 *               otherwise return 0
 * func guess(num int) int;
 */

func guessNumber(n int) int {
	start := 1
	end := n

	for start <= end {
		mid := start + (end-start)/2
		res := guess(mid)
		if res == 0 {
			return mid
		} else if res == -1 {
			end = mid - 1
		} else if res == 1 {
			start = mid + 1
		}
	}

	return -1
}
