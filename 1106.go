package main

import "fmt"

func parseBoolExpr(expression string) bool {
	var stack []string
	for _, str := range expression {
		if str == ',' {
			continue
		} else if str == ')' {
			// 弹出栈顶元素直到找到一个左括号
			var cur []string
			for len(stack) != 0 {
				if stack[len(stack)-1] != "(" {
					cur = append(cur, stack[len(stack)-1])
					stack = stack[:len(stack)-1]
				} else {
					stack = stack[:len(stack)-1]
					break
				}
			}
			// 如果栈不为空，往前取一位看是不是操作符
			if len(stack) != 0 {
				operator := stack[len(stack)-1]
				stack = stack[:len(stack)-1]
				if operator == "!" {
					// 取反，此种情况 cur 只会包含一个元素
					if cur[0] == "t" {
						stack = append(stack, "f")
					} else if cur[0] == "f" {
						stack = append(stack, "t")
					}
				} else if operator == "&" {
					// 与，有一个为 f 即为 f
					next := "t"
					for _, str := range cur {
						if str == "f" {
							next = "f"
							break
						}
					}
					stack = append(stack, next)
				} else if operator == "|" {
					// 或，有一个为 t 即为 t
					next := "f"
					for _, str := range cur {
						if str == "t" {
							next = "t"
							break
						}
					}
					stack = append(stack, next)
				}
			} else {
				// 栈为空，取与，应该不存在这种情况
			}
		} else {
			stack = append(stack, string(str))
		}
	}
	return stack[0] == "t"
}

func main() {
	fmt.Print(parseBoolExpr("!(f)"))
	fmt.Print(parseBoolExpr("|(f,t)"))
	fmt.Print(parseBoolExpr("&(t,f)"))
	fmt.Print(parseBoolExpr("|(&(t,f,t),!(t))"))
}
