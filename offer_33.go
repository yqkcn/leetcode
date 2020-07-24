package main

func verifyPostorder(postorder []int) bool {
	length := len(postorder)
	if length <= 1 {
		return true
	}
	// 左 右 根
	root := postorder[length-1]
	i := length - 2
	for ; i >= 0; i-- {
		if postorder[i] < root {
			// 此节点之前为左节点， 之后为右节点
			for j := i; j >= 0; j-- {
				if postorder[j] >= root {
					return false
				}
			}
		}
	}
	// 递归判断左右节点
	return verifyPostorder(postorder[:i+1]) && verifyPostorder(postorder[i+1:length-1])
}
