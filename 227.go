package main

import (
	"fmt"
	"strconv"
	"strings"
)

func calculate(s string) int {
	s = strings.Trim(s, " ")
	var numStack []int
	var operStack []string
	var curNum string
	for i, str := range s {
		curStr := string(str)
		// 空格无意义
		if curStr == " " {
			continue
		}
		if i == len(s) - 1 {
			curNum += curStr
			num, _ := strconv.Atoi(curNum)
			if len(operStack) == 0 {
				numStack = append(numStack, num)
				break
			}
			if operStack[len(operStack)-1] == "*" && len(numStack) != 0 {
				operStack = operStack[:len(operStack)-1]
				numStack[len(numStack)-1] *= num
				break
			} else if operStack[len(operStack)-1] == "/" && len(numStack) != 0 {
				operStack = operStack[:len(operStack)-1]
				numStack[len(numStack)-1] /= num
				break
			} else {
				numStack = append(numStack, num)
				break
			}
		}
		if curStr == "+" || curStr == "-" || curStr == "*" || curStr == "/"{
			// 数字
			num, _ := strconv.Atoi(curNum)
			// 操作符栈为空直接入栈
			// 加减暂不处理
			if len(operStack) == 0 || operStack[len(operStack)-1] == "+" || operStack[len(operStack)-1] == "-" {
				numStack = append(numStack, num)
			} else if operStack[len(operStack)-1] == "*" && len(numStack) != 0 {
				operStack = operStack[:len(operStack)-1]
				numStack[len(numStack)-1] *= num
			} else if operStack[len(operStack)-1] == "/" && len(numStack) != 0 {
				operStack = operStack[:len(operStack)-1]
				numStack[len(numStack)-1] /= num
			}
			curNum = ""
			operStack = append(operStack, curStr)
		} else {
			curNum += curStr
		}
	}
	// 只剩加减的
	for len(operStack) != 0 && len(numStack) != 0 {
		oper := operStack[0]
		operStack = operStack[1:]
		if oper == "+" {
			numStack[1] += numStack[0]
			numStack = numStack[1:]
		} else {
			numStack[1] = numStack[0] - numStack[1]
			numStack = numStack[1:]
		}
	}
	return numStack[0]
}

func main() {
	fmt.Print(calculate("0"))
}