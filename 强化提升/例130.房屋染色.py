# 问题描述
# 有n个房子在一直线上。需要给房屋染色，分别有红、蓝和绿。每个房屋染不同的颜色费用不同。需要设计一种染色
# 方案，使得相邻的房屋颜色不同，并且费用最少。返回最少的费用


# 示例
# 费用是一个n * 3的矩阵。例如cost[0][0]表示房屋0染红色的费用，cost[1][2]表示房屋1染绿色的费用。所有
# 费用均为正整数

# 输入：[[14,2,11],[11,14,5],[14,3,10]]
# 输出：10
# 解释：3个房子分别为蓝、绿、红，费用为2+5+3=10

# 输入：[[1,2,3],[1,4,6]]
# 输出：3
# 解释：两个房子分别为绿和蓝，费用为2+1=3


# 源码实现
class Solution:
    def minCost(self, costs):
        n = len(costs)
        if n == 0:
            return 0
        INF = 0x7fffffff
        f = [costs[0],[INF,INF,INF]]
        for i in range(1,n):
            for j in range(3):
                f[i&1][j] = INF
                for k in range(3):
                    if j != k:
                        f[i&1][j] = min(f[i&1][j], f[(i+1)&1][k] + costs[i][j])
        return min(f[(n - 1)&1])

# 主函数
if __name__ == '__main__':
    nums = [[14,2,11],[11,14,5],[14,3,10]]
    s = Solution()
    print("Input: ", nums)
    print("Output: ", s.minCost(nums))


# 运行结果
# Input:  [[14, 2, 11], [11, 14, 5], [14, 3, 10]]
# Output:  10