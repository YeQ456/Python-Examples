# 问题描述
# 一棵有n个节点，根节点为1的二叉树，每条边通过两个顶点x[i]、y[i]来描述，每个点的权值通过d[i]来描述。求
# 从根节点到叶子节点路径上所有节点权值乘积对10^9 + 7取模后最大路径的值


# 示例
# 输入：x = [1], y = [2], d = [1,1]
# 输出：1
# 解释：最大路径为1 -> 2, (1 + 1) % (10^9 + 7) = 1

# 输入：x = [1,2,2], y = [2,3,4], d = [1,1,-1,2]
# 输出：1000000006


# 源码实现
class Solution:
    ans = 0
    def dfs(self, x, f, g, d, mul):
        isLeaf = True
        mul = mul * d[x - 1] % 1000000007
        for i in g[x]:
            if i == f:
                continue
            isLeaf = False
            self.dfs(i, x, g, d, mul)
        if isLeaf is True:
            self.ans = max(self.ans, mul)
    
    def getProduct(self, x, y, d):
        g = [[] for i in range(len(d) + 1)]
        for i in range(len(x)):
            g[x[i]].append(y[i])
            g[y[i]].append(x[i])
        self.dfs(1, -1, g, d, 1)
        return self.ans

if __name__ == '__main__':
    x = [1,2,2]
    y = [2,3,4]
    d = [1,1,-1,2]
    s = Solution()
    print("每个边的起始和终止：", x, y)
    print("每个节点的权重：", d)
    print("最大路径上的乘积：", s.getProduct(x,y,d))


# 运行结果
# 每个边的起始和终止： [1, 2, 2] [2, 3, 4]
# 每个节点的权重： [1, 1, -1, 2]
# 最大路径上的乘积： 1000000006