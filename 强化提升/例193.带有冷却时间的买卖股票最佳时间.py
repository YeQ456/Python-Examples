# 问题描述
# 以数组表示股票价格，第i个元素表示第i天股票的价格。设计一个算法以得到最大的利润。不能同时进行多笔
# 交易（必须在再次购买之前卖出股票）。在出售股票后，无法在第2天购买股票，必须冷却1天


# 示例
# 输入：[1,2,3,0,2]
# 输出：3
# 解释：交易情况为[买，卖，停，买，卖]，第一次买卖利润为2-1=1，第2次买卖利润为2-0=2，总利润为3


# 源码实现
class Solution:
    def maxProfit(self, prices):
        if not prices:
            return 0
        buy, sell, cooldown = [0 for _ in range(len(prices))], [0 for _ in range(len(prices))], [0 for _ in range(len(prices))]
        buy[0] = -prices[0]
        for i in range(1,len(prices)):
            cooldown[i] = sell[i - 1]
            sell[i] = max(sell[i - 1], buy[i - 1] + prices[i])
            buy[i] = max(buy[i - 1], cooldown[i - 1] - prices[i])
        return max(sell[-1], cooldown[-1])

if __name__ == '__main__':
    s = Solution()
    nums = [1,2,3,0,2]
    print("输入：", nums)
    print("输出：", s.maxProfit(nums))


# 运行结果
# 输入： [1, 2, 3, 0, 2]
# 输出： 3