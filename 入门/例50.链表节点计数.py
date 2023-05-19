# 问题描述
# 计数链表中的节点数目


# 示例
# 输入：1->3->5->null
# 输出：3
# 解释：该链表有3个节点，即链表长度为3


# 源码实现
class ListNode(object):
    def __init__(self, val, next = None):
        self.val = val
        self.next = next

class Solution:
    def countNodes(self, head):
        cnt = 0
        while head is not None:
            cnt += 1
            head = head.next
        
        return cnt

# 主函数
if __name__ == '__main__':
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    solution = Solution()
    print("Input: ", node1.val, node2.val, node3.val, node4.val)
    print("Output: ", solution.countNodes(node1))



# 运行结果
# Input:  1 2 3 4
# Output:  4