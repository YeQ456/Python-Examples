# 问题描述
# 有两个用链表代表的整数，其中每个节点包含一个数字。数字存储按照原来整数中相反的顺序，使得第一个数字
# 位于链表的开头。写一个函数将两个整数相加，用链表的形式返回和


# 示例
# 输入：7->1->6->null, 5->9->2->null
# 输出：2->1->9->null
# 解释：617 + 295 = 912, 912转换成链表2->1->9->null

# 输入：3->1->5->null, 5->9->2->null
# 输出：8->0->8->null
# 解释：513 + 295 = 808, 808转换成链表：8->0->8->null


# 源码实现
class ListNode(object):
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution:
    def addLists(self, LA, LB) -> list:
        dummy = ListNode(None)
        tail = dummy
        carry = 0
        while LA or LB or carry:
            num = 0
            if LA:
                num += LA.val
                LA = LA.next
            if LB:
                num += LB.val
                LB = LB.next
            num += carry
            digit, carry = num % 10, num // 10
            node = ListNode(digit)
            tail.next, tail = node, node
        
        return dummy.next

# 主函数
if __name__ == '__main__':
    solution = Solution()
    node0 = ListNode(7)
    node1 = ListNode(1)
    node2 = ListNode(6)
    node0.next = node1
    node1.next = node2
    node3 = ListNode(5)
    node4 = ListNode(9)
    node5 = ListNode(2)
    node3.next = node4
    node4.next = node5
    ans = solution.addLists(node0,node3)
    a = [ans.val, ans.next.val, ans.next.next.val]
    print("Input: 7->1->6->null, 5->9->2->null")
    print("Output: ",a)



# 运行结果
# Input: 7->1->6->null, 5->9->2->null
# Output:  [2, 1, 9]