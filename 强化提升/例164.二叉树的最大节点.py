# 问题描述
# 在二叉树中寻找值最大的节点并返回其值


# 示例
# 输入如下二叉树：
#       1
#     /   \
#   -5     3
#   / \   / \
#  1   2 -4  -5
#
# 输出：3

# 输入如下二叉树：
#       10
#     /    \
#   -5      2
#  /  \    / \
# 0    3  -4  -5
#
# 输出：10


# 源码实现
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    
class Solution:
    def maxNode(self, root):
        if root is None:
            return root
        left = self.maxNode(root.left)
        right = self.maxNode(root.right)
        return self.max(root, self.max(left, right))
    
    def max(self, a, b):
        if a is None:
            return b
        if b is None:
            return a
        if a.val > b.val:
            return a
        return b

# 主函数
if __name__ == '__main__':
    root = TreeNode(1)
    root1 = TreeNode(-5)
    root2 = TreeNode(3)
    root3 = TreeNode(1)
    root4 = TreeNode(2)
    root5 = TreeNode(-4)
    root6 = TreeNode(-5)
    root.left = root1
    root.right = root2
    root1.left = root3
    root1.right = root4
    root2.left = root5
    root2.right = root6
    s = Solution()
    print("Input: [1,-5,3,1,2,-4,-5]")
    print("Output: ", s.maxNode(root).val)


# 运行结果
# Input: [1,-5,3,1,2,-4,-5]
# Output:  3