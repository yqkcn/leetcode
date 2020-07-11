package main

import (
	"fmt"
	"strings"
)

func reformatDate(date string) string {
	strs := strings.Split(date, " ")
	year := strs[2]
	day := strs[0][0 : len(strs[0])-2]
	if len(day) == 1 {
		day = "0" + day
	}
	month := map[string]string{
		"Jan": "01",
		"Feb": "02",
		"Mar": "03",
		"Apr": "04",
		"May": "05",
		"Jun": "06",
		"Jul": "07",
		"Aug": "08",
		"Sep": "09",
		"Oct": "10",
		"Nov": "11",
		"Dec": "12",
	}[strs[1]]
	fmt.Print(year)
	fmt.Print(month)
	fmt.Print(day)
	return year + "-" + month + "-" + day
}

func main() {
	reformatDate("20th Oct 2052")
	reformatDate("6th Jun 1933")
}
