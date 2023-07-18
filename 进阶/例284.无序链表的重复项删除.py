# 问题描述
# 设计一种方法，从无序链表中删除重复项


# 示例
# 输入：1 -> 2 -> 1 -> 3 -> 3 -> 5 -> 6 -> 3 -> null
# 输出：1 -> 2 -> 3 -> 5 -> 6 -> null


# 源码实现
class ListNode(object):
	def __init__(self, val):
		self.val = val
		self.next = None

class Solution:
	def removeDuplicates(self, head):
		seen, root, pre = set(), head, ListNode(-1)
		while head:
			if head.val not in seen:
				pre.next = head
				seen.add(head.val)
				pre = head
			head = head.next
		pre.next = None
		return root

if __name__ == '__main__':
	s = Solution()
	n0 = ListNode(1)
	n1 = ListNode(2)
	n2 = ListNode(2)
	n3 = ListNode(2)
	n0.next = n1
	n1.next = n2
	n2.next = n3
	root = s.removeDuplicates(n0)
	a = [root.val, root.next.val]
	if a == [1,2]:
		print("输入：1 -> 2 -> 2 -> 2 -> null")
		print("输出：1-> 2 -> null")
	else:
		print("Error")


# 运行结果
# 输入：1 -> 2 -> 2 -> 2 -> null
# 输出：1-> 2 -> null