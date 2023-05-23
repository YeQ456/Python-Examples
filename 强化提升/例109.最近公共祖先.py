# 问题描述
# 最近公共祖先是两个节点的公共祖先节点且具有最大深度。给定一棵二叉树，找到两个节点的最近公共
# 父节点(LCA)


# 示例
# 输入以下二叉树：
#       4
#      / \
#     3   7
#        / \
#       5   6
#
# LCA(3,5) = 4, LCA(5,6) = 7, LCA(6,7) = 7


# 源码实现
class TreeNode:
    def __init__(self, val = None, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right
    
class Solution:
    def lowestCommonAncestor(self, root, A, B):
        if root is None:
            return None
        if root == A or root == B:
            return root
        left_result = self.lowestCommonAncestor(root.left, A, B)
        right_result = self.lowestCommonAncestor(root.right, A, B)

        if left_result and right_result:
            return root
        if left_result:
            return left_result
        if right_result:
            return right_result
        return None

# 主函数
if __name__ == '__main__':
    tree = TreeNode(4, TreeNode(3), TreeNode(7, TreeNode(5), TreeNode(6)))
    s = Solution()
    result = s.lowestCommonAncestor(tree, tree.left, tree.right.left)
    print("Input: {4,3,7,#,#,5,6}, LCA(3,5)")
    print("Output: ", result.val)



# 运行结果
# Input: {4,3,7,#,#,5,6}, LCA(3,5)
# Output:  4