package main

/**
 * Forward declaration of isBadVersion API.
 * @param   version   your guess about first bad version
 * @return 	 	      true if current version is bad
 *			          false if current version is good
 * func isBadVersion(version int) bool;
 */
func isBadVersion(version int) bool {
	return true
}

func firstBadVersion(n int) int {
	res := 0
	m := 1
	for m <= n {
		mid := (m + n) / 2
		if isBadVersion(mid) {
			if !isBadVersion(mid - 1) {
				res = mid
				break
			}
			n = mid
			continue
		}
		if isBadVersion(mid + 1) {
			res = mid + 1
			break
		}
		m = mid
	}
	return res
}
