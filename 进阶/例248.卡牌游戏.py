# 问题描述
# 卡牌游戏，给出两个非负整数totalProfit(总利润)、totalCost(总成本)和n张卡牌的信息，第i张卡牌利润值a[i]
# 成本值b[i]。可以从卡牌中任意选择若干卡牌，组成一个方案，有多少个方案满足所有选择的卡牌利润和大于
# totalProfit且成本和小于totalCost


# 示例
# 输入：n = 2, totalProfit = 3, totalCost = 5, a = [2,3], b = [2,2]
# 输出：1

# 输入：n = 3, totalProfit = 5, totalCost = 10, a = [6,7,8], b = [2,3,5]
# 输出：6


# 源码实现
class Solution:
    def numOfPlan(self, n, totalProfit, totalCost, a, b):
        dp = [[0 for j in range(110)] for i in range(110)]
        dp[0][0] = 1
        mod = 1000000007
        for i in range(n):
            for j in range(totalProfit + 1, -1, -1):
                for k in range(totalCost + 1, -1, -1):
                    idxA = min(totalProfit + 1, j + a[i])
                    idxB = min(totalCost + 1, k + b[i])
                    dp[idxA][idxB] = (dp[j][k] + dp[idxA][idxB]) % mod
        ans = 0
        for i in range(totalCost):
            ans = (ans + dp[totalProfit + 1][i]) % mod
        return ans

if __name__ == '__main__':
    n = 2
    totalProfit = 3
    totalCost = 5
    a = [2,3]
    b = [2,2]
    s = Solution()
    print("总卡牌数：", n)
    print("成本和利润列表：", a, b)
    print("总成本：", totalProfit, " 需要总利润：", totalCost)
    print("可使用方法总数：", s.numOfPlan(n, totalProfit, totalCost, a, b))


# 运行结果
# 总卡牌数： 2
# 成本和利润列表： [2, 3] [2, 2]
# 总成本： 3  需要总利润： 5    
# 可使用方法总数： 1