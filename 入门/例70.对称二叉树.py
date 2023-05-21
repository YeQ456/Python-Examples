# 问题描述
# 若一棵二叉树和其镜像二叉树一样，则它是对称的。判断一个二叉树是否是对称二叉树


# 示例
# 输入：{1,2,2,3,4,4,3}
# 输出：True
#
#           1
#          / \
#         /   \
#        2     2
#       / \   / \
#      3   4 4   3

# 输入：{1,2,2,#,3,#,3}
# 输出：False
#
#           1
#          / \
#         2   2
#          \   \
#           3   3


# 源码实现
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def help(self, p, q):
        if p == None and q == None:
            return True
        if p and q and p.val == q.val:
            return self.help(p.right, q.left) and self.help(p.left, q.right)
        return False
    
    def isSymmetric(self, root):
        if root:
            return self.help(root.left, root.right)
        return True

# 主函数
if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(2)
    root.right.right = TreeNode(3)
    root.right.left = TreeNode(4)
    root.left.right = TreeNode(4)
    root.left.left = TreeNode(3)
    solution = Solution()
    print("Input: 1 2 2 3 4 4 3")
    print("Output: ", solution.isSymmetric(root))



# 运行结果
# Input: 1 2 2 3 4 4 3
# Output:  True