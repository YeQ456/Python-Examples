# 问题描述
# 计算二叉树的某层节点之和


# 示例
#        1
#       / \
#      /   \
#     2     3
#    / \   / \
#   4   5 6   7
#      /       \
#     8         9
#
# 输入：depth = 2
# 输出：5
# 解释：二叉树深度为2的所有节点之和为2+3=5

# 输入：depth = 3
# 输出：22
# 解释：4+5+6+7=22


# 源码实现
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    def levelSum(self, root, level):
        p = []
        self.dfs(root, p, 1, level)
        return sum(p)
    
    def dfs(self, root, p, dep, level):
        if root is None:
            return
        if dep == level:
            p.append(root.val)
            return
        self.dfs(root.left, p, dep + 1, level)
        self.dfs(root.right, p, dep + 1, level)

# 主函数
if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    root.left.right.right = TreeNode(8)
    root.right.right.right = TreeNode(9)
    depth = 3
    solution = Solution()
    print("Input: depth = ", depth)
    print("Output: ", solution.levelSum(root, depth))



# 运行结果
# Input: depth =  3
# Output:  22