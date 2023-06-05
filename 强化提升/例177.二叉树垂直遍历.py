# 问题描述
# 给定二叉树，返回其节点的垂直遍历顺序，即逐列从上到下。若两个节点在同一行和同一列中，则顺序为
# 从左到右


# 示例
# 输入二叉树，表示为{3,9,20,#,#,15,7}
# 输出[[9],[3,15],[20],[7]]
#       3
#     /   \
#    /     \
#   9       20
#         /    \
#        /      \
#       15       7


# 源码实现
import collections
import queue as Queue
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    def verticalOrder(self, root):
        results = collections.defaultdict(list)
        queue = Queue.Queue()
        queue.put((root, 0))
        while not queue.empty():
            node, x = queue.get()
            if node:
                results[x].append(node.val)
                queue.put((node.left, x - 1))
                queue.put((node.right, x + 1))
        return [results[i] for i in sorted(results)]

# 主函数
if __name__ == '__main__':
    root = TreeNode(3)
    root1 = TreeNode(9)
    root2 = TreeNode(20)
    root3 = TreeNode(15)
    root4 = TreeNode(7)
    root.left = root1
    root.right = root2
    root2.left = root3
    root2.right = root4
    s = Solution()
    a = s.verticalOrder(root)
    print("Input: [3,9,20,#,#,15,7]")
    print("Output: ", a)


# 运行结果
# Input: [3,9,20,#,#,15,7]
# Output:  [[9], [3, 15], [20], [7]]