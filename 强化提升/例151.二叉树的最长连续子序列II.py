# 问题描述
# 给出一棵k叉树，找到最长连续序列路径的长度。路径的开头和结尾可以是树的任意节点


# 示例
# 输入：k叉树，5<6<7<>,5<>,8<>>,4<3<>,5<>,31<>>>
# 输入：5
# 解释：
#          5
#         /  \
#        /    \
#       6      4
#     / | \   /|\
#    7  5  8 3 5 3
# 最长路径：3--4--5--6--7


# 源码实现
class MultiTreeNode(object):
    def __init__(self, x):
        self.val = x
        self.children = []
    
class Solution:
    def longestConsecutive(self, root):
        max_len, _, _ = self.helper(root)
        return max_len

    def helper(self, root):
        if root is None:
            return 0,0,0
        max_len, up, down = 0,0,0
        for child in root.children:
            result = self.helper(child)
            max_len = max(max_len, result[0])
            if child.val + 1 == root.val:
                down = max(down, result[1] + 1)
            if child.val - 1 == root.val:
                up = max(up, result[2] + 1)
        max_len = max(down + 1 + up, max_len)
        return max_len, down, up

# 主函数
if __name__ == '__main__':
    root = MultiTreeNode(5)
    root1 = MultiTreeNode(6)
    root2 = MultiTreeNode(4)
    root3 = MultiTreeNode(7)
    root4 = MultiTreeNode(5)
    root5 = MultiTreeNode(8)
    root6 = MultiTreeNode(3)
    root7 = MultiTreeNode(5)
    root8 = MultiTreeNode(3)
    root.children = [root1,root2]
    root1.children = [root3,root4,root5]
    root2.children = [root6,root7,root8]
    s = Solution()
    print("Input: 5<6<7<>,5<>,8<>>,4<3<>,5<>,31<>>>")
    print("Output: ", s.longestConsecutive(root))


# 运行结果
# Input: 5<6<7<>,5<>,8<>>,4<3<>,5<>,31<>>>
# Output:  5