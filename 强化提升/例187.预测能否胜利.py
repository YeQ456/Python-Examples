# 问题描述
# 给一个非负整数构成的数组，玩家1从数组的任意一端选择一个数字，玩家2从数组的任意一端选择一个数字，
# 轮流进行。每次一个玩家只能取一个数，每个数只能取一次。数组内分数都被取完后，总数大的玩家获胜。
# 给定数组，预测玩家1能否胜利。数组长度大于或等于1且小于或等于20，任意数均为非负数且不超过
# 10000000.若两个玩家分数相同，则玩家1获胜


# 示例
# 输入：[1,5,2]
# 输出：False
# 解释：玩家1可以选择1或2,若他选择2(或1),则玩家2可以选择1(2)或5，若玩家2选择了5，则玩家1只能选择1(或2)
# 所以玩家1最终的分数为1 + 2 = 3，而玩家2为5，玩家1不能赢，返回False


# 源码实现
class Solution:
    def predictTheWinner(self, nums):
        if len(nums) & 1 == 0:
            return True
        dp = [[0] * len(nums) for _ in range(len(nums))]
        for i, v in enumerate(nums):
            dp[i][i] = v
        for i in range(1, len(nums)):
            for j in range(len(nums) - i):
                dp[j][j + i] = max(nums[j] - dp[j + 1][j + i], nums[j + i] - dp[j][j + i - 1])
        return dp[0][-1] > 0

# 主函数
if __name__ == '__main__':
    nums = [1,5,2]
    s = Solution()
    print("输入：", nums)
    print("输出：", s.predictTheWinner(nums))


# 运行结果
# 输入： [1, 5, 2]
# 输出： False