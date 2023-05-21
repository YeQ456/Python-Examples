# 问题描述
# 将两个有序链表合并为一个新的有序链表


# 示例
# 输入：list1=1->3->8->11->15->null, list2=2->null
# 输出：1->2->3->8->11->15->null


# 源码实现
class ListNode(object):
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution(object):
    def mergeTwoLists(self, LA, LB):
        dummy = ListNode(0)
        tmp = dummy
        while LA != None and LB != None:
            if LA.val < LB.val:
                tmp.next = LA
                LA = LA.next
            else:
                tmp.next = LB
                LB = LB.next
            tmp = tmp.next
        
        if LA != None:
            tmp.next = LA
        else:
            tmp.next = LB
        
        return dummy.next

# 主函数
if __name__ == '__main__':
    solution = Solution()
    node0 = ListNode(1)
    node1 = ListNode(3)
    node2 = ListNode(8)
    node0.next = node1
    node1.next = node2
    node5 = ListNode(2)
    node6 = ListNode(4)
    node5.next = node6
    ans = solution.mergeTwoLists(node0,node5)
    a = [ans.val,ans.next.val,ans.next.next.val,ans.next.next.next.val,ans.next.next.next.next.val]
    print("Input: list1=1->3->8->null, list2=2->4->null")
    print("Output: ", a)



# 运行结果
# Input: list1=1->3->8->null, list2=2->4->null
# Output:  [1, 2, 3, 4, 8]