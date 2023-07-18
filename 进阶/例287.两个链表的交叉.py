# 问题描述
# 写一个方法找到两个单链表最初的交叉节点并返回该节点。若两个链表没有交叉，则返回null


# 示例
# 输入AB两个链表：
# A: a1 -> a2
# B:       b1 -> b2 -> b3    ===> c1 -> c2 -> c3
# 输出：c1


# 源码实现
class ListNode:
	def __init__(self, val = None, next = None):
		self.value = val
		self.next = next

class Solution:
	def get_list_length(self, head):
		length = 0
		while head:
			length += 1
			head = head.next
		return length

	def get_intersect_node(self, list_a, list_b):
		length_a = self.get_list_length(list_a)
		length_b = self.get_list_length(list_b)
		cur1, cur2 = list_a, list_b
		if length_a > length_b:
			for i in range(length_a - length_b):
				cur1 = cur1.next
		else:
			for i in range(length_b - length_a):
				cur2 = cur2.next
		flag = False
		while cur1 and cur2:
			if cur1.value == cur2.value:
				print(cur1.value)
				flag = True
				break
			else:
				cur1 = cur1.next
				cur2 = cur2.next
		if not flag:
			print('链表没有交叉节点')

if __name__ == '__main__':
	s = Solution()
	list_a = ListNode('a1', ListNode('a2', ListNode('c1', ListNode('c2', ListNode('c3')))))
	list_b = ListNode('b1', ListNode('b2', ListNode('b3', ListNode('c1', ListNode('c2', ListNode('c3'))))))
	print("输入：")
	print("a = a1 a2 c1 c2 c3")
	print("b = b1 b2 b3 c1 c2 c3")
	print("输出：")
	s.get_intersect_node(list_a, list_b)


# 运行结果
# 输入：
# a = a1 a2 c1 c2 c3
# b = b1 b2 b3 c1 c2 c3
# 输出：
# c1