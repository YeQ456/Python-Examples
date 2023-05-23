# 问题描述
# 给出一棵二叉树，返回其节点值，自底向上的层次遍历，即按从叶子节点所在层到根节点所在层遍历，
# 然后逐层从左向右遍历


# 示例
# 输入：{1,2,3}
# 输出：[[2,3],[1]]
#       1
#      / \
#     2   3

# 输入：{3,9,20,#,#,15,7}
# 输出：[[15,7],[9,20],[3]]
#       3
#      / \
#     9   20
#        /  \
#       15   7


# 源码实现
class TreeNode:
    def __init__(self, val = None, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrderBottom(self, root):
        self.results = []
        if not root:
            return self.results
        q = [root]
        while q:
            new_q = []
            self.results.append([n.val for n in q])
            for node in q:
                if node.left:
                    new_q.append(node.left)
                if node.right:
                    new_q.append(node.right)
            q = new_q
        return list(reversed(self.results))

# 主函数
if __name__ == '__main__':
    s = Solution()
    root = TreeNode(1, TreeNode(2), TreeNode(3))
    result = s.levelOrderBottom(root)
    print("Input: {1,2,3}")
    print("Output: ", result)



# 运行结果
# Input: {1,2,3}
# Output:  [[2, 3], [1]]