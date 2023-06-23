# 问题描述
# 给定具有重复项的二叉搜索树(BST)，找到BST中的所有modes(出现最频繁的元素)。


# 示例
# 输入：[1,#,2,2]
# 输出：[2]


# 源码实现
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    def helper(self, root, cache):
        if root == None:
            return
        cache[root.val] += 1
        self.helper(root.left, cache)
        self.helper(root.right, cache)
        return
    
    def findMode(self, root):
        from collections import defaultdict
        if root == None:
            return []
        cache = defaultdict(int)
        self.helper(root, cache)
        max_freq = max(cache.values())
        result = [k for k, v in cache.items() if v == max_freq]
        return result

if __name__ == '__main__':
    T = TreeNode(1)
    T.left = None
    T2 = TreeNode(2)
    T.right = T2
    T3 = TreeNode(2)
    T2.left = T3
    s = Solution()
    print("输入：{1,#,2,2}")
    print("输出：", s.findMode(T))


# 运行结果
# 输入：{1,#,2,2}
# 输出： [2]