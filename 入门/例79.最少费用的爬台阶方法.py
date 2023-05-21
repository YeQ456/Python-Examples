# 问题描述
# 在楼梯上，每一号台阶都有各自的费用，即第i号(台阶从0号索引)台阶有非负成本cost[i].一旦支付了费用，可以
# 爬1~2步。需要找到最低成本来达到最高层。从索引为0的楼梯开始，也可以从索引为1的楼梯开始


# 示例
# 输入：cost = [10,15,20]
# 输出：15
# 解释：最便宜的方法是从第1号台阶起步，支付费用并直接到达顶层

# 输入：cost = [1,100,1,1,1,100,1,1,100,1]
# 输出：6
# 解释：最便宜的方法是从第0号台阶起步，只走费用为1的台阶并且跳过第3号台阶


# 源码实现
class Solution:
    # 状态转移方程：
    # dp[i] = min(dp[i - 1] + cost[i - 1], dp[i - 2] + cost[i - 2])
    def minCostClimbingStairs(self, cost):
        a,b = 0,0
        for i in range(2, len(cost) + 1):
            c = min(a + cost[i - 2], b + cost[i - 1])
            a,b = b,c
        return b

# 主函数
if __name__ == '__main__':
    solution = Solution()
    cost = [1,100,1,1,1,100,1,1,100,1]
    print("Input: cost = ", cost)
    print("Output: ", solution.minCostClimbingStairs(cost))



# 运行结果
# Input: cost =  [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
# Output:  6