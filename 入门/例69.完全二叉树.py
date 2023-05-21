# 问题描述
# 完全二叉树特点：只允许最后一层有空缺节点且空缺在右边，即叶子节点只能在层次最大的两层上出现；对任一节点，
# 若其右子树深度为j，则其左子树的深度必为j或j+1，即度为1的点只有1个或者0个。判断一个二叉树是否是完全
# 二叉树


# 示例
# 输入：二叉树为{1,2,3,4}
#
#       1
#      / \
#     2   3
#    /
#   4
#
# 输出：True

# 输入：{1,2,3,#,4}
#
#       1
#      / \
#     2   3
#      \
#       4
#
# 输出：False


# 源码实现
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
    
class Solution:
    def isComplete(self, root):
        if root is None:
            return True
        queue = [root]
        index = 0
        while index < len(queue):
            if queue[index] is not None:
                queue.append(queue[index].left)
                queue.append(queue[index].right)
            index += 1
        
        while queue[-1] is None:
            queue.pop()
        for q in queue:
            if q is None:
                return False
        
        return True

# 主函数
if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    solution = Solution()
    print("Input: 1 2 3 4")
    print("Output: ", solution.isComplete(root))



# 运行结果
# Input: 1 2 3 4
# Output:  True