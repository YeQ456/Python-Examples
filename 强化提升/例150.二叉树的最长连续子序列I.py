# 问题描述
# 给定一棵二叉树，找到最长连续序列的长度（节点数）。路径起点和终点可以为二叉树的任意节点


# 示例
# 输入：{1,2,0,3}
# 输出：4
# 解释：
#       1
#      / \
#     2   0
#    /
#   3
# 最长连续序列路径：0-1-2-3，故长度为4


# 源码实现
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def longestConsecutive(self, root):
        max_len, i, j = self.helper(root)
        return max_len
    
    def helper(self, root):
        if root is None:
            return 0,0,0
        left_len, left_down, left_up = self.helper(root.left)
        right_len, right_down, right_up = self.helper(root.right)
        down, up = 0, 0
        if root.left is not None and root.left.val + 1 == root.val:
            down = max(down, left_down + 1)
        if root.left is not None and root.left.val - 1 == root.val:
            up = max(up, left_up + 1)
        if root.right is not None and root.right.val + 1 == root.val:
            down = max(down, right_down + 1)
        if root.right is not None and root.right.val - 1 == root.val:
            up = max(up, right_up + 1)
        len = down + 1 + up
        len = max(len, left_len, right_len)
        return len, down, up

# 主函数
if __name__ == '__main__':
    nums = {1,2,0,3}
    root0 = TreeNode(0)
    root1 = TreeNode(1)
    root2 = TreeNode(2)
    root3 = TreeNode(3)
    root1.left = root2
    root1.right = root0
    root2.left = root3
    s = Solution()
    print("Input: ", nums)
    print("Output: ", s.longestConsecutive(root1))


# 运行结果
# Input:  {0, 1, 2, 3}
# Output:  4