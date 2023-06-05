# 问题描述
# 给出一个二叉树，其中所有右节点可能是具有兄弟节点的叶子节点(即有一个相同父节点的左节点)或空白。将
# 其倒置并转换为树，其中原来的右节点变为左叶子节点。返回新的根节点


# 示例
# 给出一个二叉树，表示为{1,2,3,4,5}
#       1
#      / \
#     2   3
#    / \
#   4   5
# 返回二叉树，表示为{4,5,2,#,#,3,1}
#      4
#     / \
#    5   2
#       / \
#      3   1


# 源码实现
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
    
class Solution:
    def upsideDownBinaryTree(self, root):
        if root is None:
            return None
        return self.dfs(root)
    
    def dfs(self, root):
        if root.left is None:
            return root
        newRoot = self.dfs(root.left)
        root.left.right = root
        root.left.left = root.right
        root.left = None
        root.right = None
        return newRoot

# 主函数
if __name__ == '__main__':
    root1 = TreeNode(1)
    root2 = TreeNode(2)
    root3 = TreeNode(3)
    root4 = TreeNode(4)
    root5 = TreeNode(5)
    nums = [1,2,3,4,5,"#","#"]
    root1.left = root2
    root1.right = root3
    root2.left = root4
    root2.right = root5
    s = Solution()
    a = s.upsideDownBinaryTree(root1)
    a0 = a.val
    a1 = a.left.val
    a2 = a.right.val
    a3 = '#'
    a4 = '#'
    a5 = a.right.left.val
    a6 = a.right.right.val
    aa = [a0,a1,a2,a3,a4,a5,a6]
    print("Input: ", nums)
    print("Output: ", aa)


# 运行结果
# Input:  [1, 2, 3, 4, 5, '#', '#'] 
# Output:  [4, 5, 2, '#', '#', 3, 1]