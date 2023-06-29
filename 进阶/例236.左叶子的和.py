# 问题描述
# 找出给定二叉树中所有左叶子值之和


# 示例
# 输入：
#      3
#     / \
#    9   20
#       /  \
#      15   7
# 输出：24
# 解释：9 + 15 = 24


# 源码实现
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
    
class Solution(object):
    def sumOfLeftLeaves(self, root):
        def dfs(root):
            if not root:
                return 0
            sum = 0
            if root.left:
                left = root.left
                if not left.left and not left.right:
                    sum += left.val
                else:
                    sum += dfs(left)
            if root.right:
                right = root.right
                sum += dfs(right)
            return sum
        return dfs(root)

if __name__ == '__main__':
    s = Solution()
    t = TreeNode(3)
    t1 = TreeNode(9)
    t.left = t1
    t2 = TreeNode(20)
    t.right = t2
    t3 = TreeNode(15)
    t2.left = t3
    t4 = TreeNode(7)
    t2.right = t4
    print("输入：[3,9,20,# # 15 7]")
    print("输出：", s.sumOfLeftLeaves(t))


# 运行结果
# 输入：[3,9,20,# # 15 7]
# 输出： 24