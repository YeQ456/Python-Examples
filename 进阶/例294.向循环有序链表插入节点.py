# 问题描述
# 给定有序的循环链表，写一个函数将一个值插入循环链表中，使循环链表保持有序。给出链表的任意起始节点，返回插入后的新链表


# 示例
# 输入：3 -> 5 -> 1, 需要插入4
# 输出：3 -> 4 -> 5 -> 1


# 源码实现
class ListNode:
	def __init__(self, val = None, next = None):
		self.val = val
		self.next = next

class Solution:
	def insert(self, node, x):
		new_node = ListNode(x)
		if node is None:
			node = new_node
			node.next = node
			return node
		cur, pre = node, None
		while cur:
			pre = cur
			cur = cur.next
			if x <= cur.val and x >= pre.val:
				break
			if pre.val > cur.val and (x < cur.val or x > pre.val):
				break
			if cur is node:
				break
		new_node.next = cur
		pre.next = new_node
		return new_node

if __name__ == '__main__':
	k = 4
	generator = ListNode(3, ListNode(5, ListNode(1)))
	s = Solution()
	s.insert(generator, k)
	print("输入：{3,5,1}")
	print("输出：", generator.val, generator.next.val, generator.next.next.val, generator.next.next.next.val)


# 运行结果
# 输入：{3,5,1}
# 输出： 3 4 5 1