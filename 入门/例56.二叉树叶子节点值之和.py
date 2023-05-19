# 问题描述
# 叶子节点是一棵树中没有子节点（即度为0）的节点，也即是一个二叉树任意一个分支上的终端节点。
# 计算二叉树的叶子节点值之和


# 输入：
#       1
#      / \
#     2   3
#    /
#   4
#
# 输出：7


# 输入：
#       1
#        \
#         3
#
# 输出：3


# 源码实现
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
    
class Solution:
    def leafSum(self, root):
        p = []
        self.dfs(root, p)
        return sum(p)
    
    def dfs(self, root, p):
        if root is None:
            return
        if root.left is None and root.right is None:
            p.append(root.val)
        self.dfs(root.left, p)
        self.dfs(root.right, p)

# 主函数
if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    solution = Solution()
    print("Input: ", root.val, root.left.val, root.right.val, root.left.left.val)
    print("Output: ", solution.leafSum(root))



# 运行结果
# Input:  1 2 3 4
# Output:  7