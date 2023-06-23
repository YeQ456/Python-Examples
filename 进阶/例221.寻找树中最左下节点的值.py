# 问题描述
# 给定一棵二叉树，找到这棵树最后一行中最左边的值


# 示例
# 如下图，查找的值为4
#       1
#      / \
#     2   3
#    / \
#   4   5


# 源码实现
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    def findBottomLeftValue(self, root):
        self.max_level = 0
        self.val = None
        self.helper(root, 1)
        return self.val

    def helper(self, root, level):
        if not root:
            return
        if level > self.max_level:
            self.max_level = level
            self.val = root.val
        self.helper(root.left, level + 1)
        self.helper(root.right, level + 1)

if __name__ == '__main__':
    node = TreeNode(1)
    node.left = TreeNode(2)
    node.right = TreeNode(3)
    node.left.left = TreeNode(4)
    s = Solution()
    print("输入：[1,2,3,4 # # #]")
    print("输出：", s.findBottomLeftValue(node))


# 运行结果
# 输入：[1,2,3,4 # # #]
# 输出： 4