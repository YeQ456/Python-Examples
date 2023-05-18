# 问题描述
# 给定一棵二叉树，寻找最长连续路径的长度，即任何序列起点到树种任一节点都必须遵循父-子关系，
# 最长的连续路径必须是从父节点到子节点


# 示例
# 输入：{1,#,3,2,4,#,#,#,5}
# 输出：3
# 解释：
#       1
#        \
#         3
#        / \
#       2   4
#            \
#             5
# 
# 最长连续序列：3 - 4 - 5

# 源码实现
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def longestConsecutive(self, root):
        return self.helper(root, None, 0)
    
    def helper(self, root, parent, len):
        if root is None:
            return len
        if parent != None and root.val == parent.val + 1:
            len += 1
        else:
            len = 1

        return max(len, max(self.helper(root.left, root, len), self.helper(root.right, root, len)))

# 主函数
if __name__ == '__main__':
    root = TreeNode(1)
    root.right = TreeNode(3)
    root.right.left = TreeNode(2)
    root.right.right = TreeNode(4)
    root.right.right.right = TreeNode(5)
    solution = Solution()
    print("Input: {1,#,3,2,4,#,#,#,5}")
    print("Output: ", solution.longestConsecutive(root))



# 运行结果
# Input: {1,#,3,2,4,#,#,#,5}
# Output:  3