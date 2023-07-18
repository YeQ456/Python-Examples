# 问题描述
# 给定一个单链表中一个等待被删除的节点（非表头或表尾）。请在O(1)时间复杂度删除该链表节点


# 示例
# 输入：1 -> 2 -> 3 -> 4 -> null, 删除节点3
# 输出：1 -> 2 -> 4 -> null


# 源码实现
class ListNode(object):
	def __init__(self, val, next = None):
		self.val = val
		self.next = next

class Solution:
	def deleteNode(self, node):
		if node.next is None:
			node = Nonde
			return
		node.val = node.next.val
		node.next = node.next.next

if __name__ == '__main__':
	n1 = ListNode(1)
	n2 = ListNode(2)
	n3 = ListNode(3)
	n4 = ListNode(4)
	n1.next = n2
	n2.next = n3
	n3.next = n4
	s = Solution()
	print("输入：", n1.val, n2.val, n3.val, n4.val)
	s.deleteNode(n3)
	print("删除节点3")
	print("输出：", n1.val, n2.val, n3.val)


# 运行结果
# 输入： 1 2 3 4
# 删除节点3
# 输出： 1 2 4