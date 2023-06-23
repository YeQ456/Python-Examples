# 问题描述
# 给定一棵树的根，找到出现频率最高的子树和[由以该节点为根的子树(包括节点本身)形成的所有节点值的总和]。
# 若存在多个，则以任意顺序返回频率最高的所有值


# 示例
# 输入：{5,2,-3}
# 输出：[-3,2,4]
# 解释：如下图，所有的值都出现了一次，则可以任意顺序返回
#       5
#      / \
#     2  -3


# 源码实现
import collections
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    def findFrequentTreeSum(self, root):
        if not root:
            return []
        counter = collections.Counter()
        def sumnode(node):
            if not node:
                return 0
            ret = node.val
            if node.left:
                ret += sumnode(node.left)
            if node.right:
                ret += sumnode(node.right)
            counter[ret] += 1
            return ret
        sumnode(root)
        arr = []
        for k in counter:
            arr.append((k, counter[k]))
        arr.sort(key = lambda x: x[1], reverse = True)
        i = 0
        while i + 1 < len(arr) and arr[i + 1][1] == arr[0][1]:
            i += 1
        return [x[0] for x in arr[:i+1]]

if __name__ == '__main__':
    node = TreeNode(5)
    node.right = TreeNode(-3)
    node.left = TreeNode(2)
    s = Solution()
    print("输入：{5,-3,2}")
    print("输出：", s.findFrequentTreeSum(node))


# 运行结果
# 输入：{5,-3,2}
# 输出： [2, -3, 4]