# 问题描述
# 猜数游戏规则：从1~n选一个数字，需要猜选择了哪一个。每次猜错都会提示该数字是高还是低。而当猜错这个数字
# 时，需要支付$x，当猜对数字时则赢下这场游戏。现给定一个具体数字，计算需要多少钱才能保证赢得比赛


# 示例
# 输入：n = 10，选择的数字为2
# 第1轮：猜7，提示数字大了，支付$7；第2轮，猜3，提示数字大了，支付$3,；第3轮：猜1，提示数字小了
# 支付$1；游戏结束，2是所猜数字，则最终需要支付$11


# 源码实现
class Solution:
    def getMoneyAmount(self, n):
        dp = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
        for len in range(2, n + 1):
            for start in range(1, n - len + 2):
                import sys
                temp = sys.maxsize
                for k in range(start + int((len - 1) / 2), start + int(len - 1)):
                    left, right = dp[start][k - 1], dp[k + 1][start + len - 1]
                    temp = min(k + max(left, right), temp)
                    if left > right:
                        break
                    dp[start][start + len - 1] = temp
        return dp[1][n]

# 主函数
if __name__ == '__main__':
    num = 10
    s = Solution()
    print("输入：", num)
    print("输出：", s.getMoneyAmount(num))


# 运行结果
# 输入： 10
# 输出： 16