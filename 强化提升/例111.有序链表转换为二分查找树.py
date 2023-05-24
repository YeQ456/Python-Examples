# 问题描述
# 给出一个所有元素以升序排列的单链表，将它转换成一棵高度平衡的二分查找树


# 示例
# 例如：
#                 2
# 1->2->3  =>    / \
#               1   3


# 源码实现
class ListNode(object):
    def __init__(self, val, next = None):
        self.val = val
        self.next = next

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    def sortedListToBST(self, head):
        num_list = []
        while head:
            num_list.append(head.val)
            head = head.next
        return self.create(num_list, 0, len(num_list) - 1)
    
    def create(self, nums, start, end):
        if start > end:
            return None
        if start == end:
            return TreeNode(nums[start])
        root = TreeNode(nums[(start + end) // 2])
        root.left = self.create(nums, start, (start + end) // 2 - 1)
        root.right = self.create(nums, (start + end) // 2 + 1, end)
        return root

# 主函数
if __name__ == '__main__':
    s = Solution()
    listnode = ListNode(1, ListNode(2, ListNode(3)))
    root = s.sortedListToBST(listnode)
    print("Input: 1->2->3")
    print("Output: {", root.val, root.left.val, root.right.val, "}")



# 运行结果
# Input: 1->2->3
# Output: { 2 1 3 }