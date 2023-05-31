# 问题描述
# 给定二叉树，找出二叉树中的一棵子树，使其所有节点之和最大，返回这课子树的根节点


# 示例
# 输入如下二叉树
#       1
#     /   \
#   -5      2
#   / \    / \
#  0   3 -4  -5
#
# 输出：3


# 源码实现
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    
class Solution:
    import sys
    maximum_weight = 0
    result = None
    def findSubtree(self, root):
        self.helper(root)
        return self.result.val
    
    def helper(self, root):
        if root is None:
            return 0
        left_weight = self.helper(root.left)
        right_weight = self.helper(root.right)
        if left_weight + right_weight + root.val >= self.maximum_weight or self.result is None:
            self.maximum_weight = left_weight + right_weight + root.val
            self.result = root
        
        return left_weight + right_weight + root.val

# 主函数
if __name__ == '__main__':
    root = TreeNode(1)
    root1 = TreeNode(-5)
    root2 = TreeNode(2)
    root3 = TreeNode(0)
    root4 = TreeNode(3)
    root5 = TreeNode(-4)
    root6 = TreeNode(-5)
    root.left = root1
    root.right = root2
    root1.left = root3
    root1.right = root4
    root2.left = root5
    root2.right = root6
    s = Solution()
    print("Input: [1, -5, 2, 0, 3, -4, -5]")
    print("Output: ", s.findSubtree(root))


# 运行结果
# Input: [1, -5, 2, 0, 3, -4, -5]
# Output:  3