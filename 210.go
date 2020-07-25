package main

func findOrder(numCourses int, prerequisites [][]int) []int {
	pres := make(map[int][]int)
	for i:=0;i<numCourses;i++{
		pres[i] = []int{}
	}
	// 遍历一遍，统计前序课程
	for _, nums := range prerequisites {
		pres[nums[0]] = append(pres[nums[0]], nums[1])
	}
	// 深搜
	return dfs(numCourses, pres, []int{}, make(map[int]bool))
}

func dfs(numCourses int, pres map[int][]int, courses []int, cache map[int]bool) []int {
	if len(courses) == numCourses {
		return courses
	}
	for i:=0;i<numCourses;i++{
		// 已学习
		if cache[i] {
			continue
		} else if isValid(pres, cache, i) {
				courses = append(courses, i)
				cache[i] = true
				next := dfs(numCourses, pres, courses, cache)
				// ok
				if len(next) == numCourses {
					return next
				}
				courses = courses[:len(courses)-1]
				delete(cache, i)
				continue
		}
	}
	return []int{}
}

func isValid(pres map[int][]int, cache map[int]bool, i int) bool {
	pre, _ := pres[i]
	if len(pre) == 0 {
		return true
	}
	for _, num := range pre {
		if !cache[num] {
			return false
		}
	}
	return true
}