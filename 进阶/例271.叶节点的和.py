# 问题描述
# 给出一棵二叉树，求所有叶节点的和


# 示例
# 输入二叉树：
# 		1
#      / \
#     2   3
#    / \
#   4   5
#
# 输出：12


# 源码实现
class TreeNode:
	def __init__(self, val):
		self.val = val
		self.left, self.right = None, None

class Solution:
	def sumLeafNode(self, root):
		res = 0
		p = root
		while p:
			if p.left is None:
				if p.right is None:
					res += p.val
				p = p.right
			else:
				tmp = p.left
				while tmp.right is not None and tmp.right != p:
					tmp = tmp.right
				if tmp.right is None:
					if tmp.left is None:
						res += tmp.val
					tmp.right = p
					p = p.left
				else:
					tmp.right = None
					p = p.right
		return res

if __name__ == '__main__':
	n1 = TreeNode(1)
	n1.left = TreeNode(2)
	n1.right = TreeNode(3)
	n1.left.left = TreeNode(4)
	n1.left.right = TreeNode(5)
	s = Solution()
	print("结果：", s.sumLeafNode(n1))


# 运行结果
# 结果： 12