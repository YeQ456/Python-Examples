# 问题描述
# 深度复制一棵二叉树。


# 示例
#       1
#      / \
#     2   3
#    / \
#   4   5
#
# 输入：{1,2,3,4,5}
# 输出：{1,2,3,4,5}


# 源码实现
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
    
class Solution:
    def cloneTree(self, root):
        if root is None:
            return None
        
        clone_root = TreeNode(root.val)
        clone_root.left = self.cloneTree(root.left)
        clone_root.right = self.cloneTree(root.right)
        return clone_root

# 主函数
if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    solution = Solution()
    print("Input: 1 2 3 4 5", )
    print("Output: ", solution.cloneTree(root).val, solution.cloneTree(root).left.val, solution.cloneTree(root).right.val, solution.cloneTree(root).left.left.val, solution.cloneTree(root).left.right.val)



# 运行结果
# Input: 1 2 3 4 5
# Output:  1 2 3 4 5