# 问题描述
# 检查两棵二叉树在经过若干次扭转后是否可以等价。扭转的定义：交换任意节点的左右子树。等价的定义：两棵
# 二叉树必须为相同的结构，并且对应位置上的节点值要相等


# 示例
# 输入：{1,2,3,4},{1,3,2,#,#,#,4}
# 输出：True
# 解释：
#       1             1
#      / \           / \
#     2   3         3   2
#    /                   \
#   4                     4
#
# 扭转第2层节点左右子树可以变换为等价的

# 输入：{1,2,3,4},{1,3,2,4}
# 输出：False
# 解释：扭转第2层节点左右子树不能变换为等价的


# 源码实现
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def isTweakedIdentical(self, a, b):
        if a == None and b == None:
            return True
        if a and b and a.val == b.val:
            return self.isTweakedIdentical(a.left,b.left) and \
                   self.isTweakedIdentical(a.right, b.right) or \
                   self.isTweakedIdentical(a.left,b.right) and \
                   self.isTweakedIdentical(a.right,b.left)
        return False

# 主函数
if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root1 = TreeNode(1)
    root1.right = TreeNode(2)
    root1.left = TreeNode(3)
    root1.right.right = TreeNode(4)
    solution = Solution()
    print("Input: 1 2 3 4, 1 3 2 4")
    print("Output: ", solution.isTweakedIdentical(root,root1))



# 运行结果
# Input: 1 2 3 4, 1 3 2 4
# Output:  True