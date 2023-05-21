# 问题描述
# 找到单链表倒数第n个节点，保证链表中的节点的最少数量为n


# 示例
# 输入：list = 3->2->1->5->null, n = 2
# 输出：1

# 输入：list = 1->2->3->null, n = 3
# 输出：1


# 源码实现
class ListNode(object):
    def __init__(self, val):
        self.val = val
        self.next = None
    
class Solution:
    def nthToLast(self, head, n):
        if head is None or n < 1:
            return None
        cur = head.next
        while cur is not None:
            cur.pre = head
            cur = cur.next
            head = head.next
        n -= 1
        while n > 0:
            head = head.pre
            n -= 1
        return head

# 主函数
if __name__ == '__main__':
    solution = Solution()
    head = ListNode(3)
    node1 = ListNode(2)
    node2 = ListNode(1)
    node3 = ListNode(5)
    head.next = node1
    node1.next = node2
    node2.next = node3
    ans = solution.nthToLast(head, 2).val
    print("Input: 3->2->1->5->null, n = 2")
    print("Output: ", ans)



# 运行结果
# Input: 3->2->1->5->null, n = 2
# Output:  1