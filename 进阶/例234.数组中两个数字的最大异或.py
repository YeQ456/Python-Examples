# 问题描述
# 给定一个非空数组[a0,a1,a2,...,an-1]，其中0 <= ai <= 2^31.找出ai XOR aj的最大结果，其中0 <= i,j < n


# 示例
# 输入[3,10,5,25,2,8]
# 输出：28
# 解释：最大的结果为5XOR25 = 28


# 源码实现
import sys
class TrieNode:
    def __init__(self, val):
        self.val = val
        self.children = {}
    
class Solution:
    def findMaximumXOR(self, nums):
        answer = 0
        for i in range(32)[::-1]:
            answer <<= 1
            prefixes = {num >> i for num in nums}
            answer += any(answer^1 ^ p in prefixes for p in prefixes)
        return answer
    
    def findMaximumXOR_TLE(self, nums):
        root = TrieNode(0)
        for num in nums:
            self.addNode(root, num)
        res = -sys.maxsize
        for num in nums:
            cur_node, cur_sum = root, 0
            for i in reversed(range(0, 32)):
                bit = (num >> i) & 1
                if (bit ^ 1) in cur_node.children:
                    cur_sum += 1 << i
                    cur_node = cur_node.children[bit ^ 1]
                else:
                    cur_node = cur_node.children[bit]
            res = max(res, cur_sum)
        return res
    
    def addNode(self, root, num):
        cur = root
        for i in reversed(range(0, 32)):
            bit = (num >> i) & 1
            if bit not in cur.children:
                cur.children[bit] = TrieNode(bit)
            cur = cur.children[bit]

if __name__ == '__main__':
    s = Solution()
    n = [3,10,5,25,2,8]
    print("输入：", n)
    print("输出：", s.findMaximumXOR(n))


# 运行结果
# 输入： [3, 10, 5, 25, 2, 8]
# 输出： 28