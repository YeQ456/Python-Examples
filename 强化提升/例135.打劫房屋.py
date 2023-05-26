# 问题描述
# 将打劫房屋围成一圈，即第一间房屋和最后一间房屋是挨着的。每个房屋都存放着特定金额的钱。面临的唯一约束
# 条件是：相邻的房屋装着相互联系的防盗系统，且当相邻的两个房屋同一天被打劫时，该系统会自动报警。给定
# 一个非负整数列表，表示每个房屋中存放的钱，若今晚去打劫，在不触碰报警系统装置的情况下，最多可以得到
# 多少钱


# 示例
# 输入：nums = [3,6,4]
# 输出：6
# 解释：只能打劫房屋2，获得钱数为6

# 输入：nums = [2,3,2,3]
# 输出：6
# 解释：只能打劫房屋2和4，获得钱数为3+3=6


# 源码实现
class Solution:
    def houseRobber(self, nums):
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        dp = [0] * n
        dp[0], dp[1] = 0, nums[1]
        for i in range(2, n):
            dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])
        answer = dp[n - 1]
        dp[0], dp[1] = nums[0], max(nums[0], nums[1])
        for i in range(2, n - 1):
            dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])
        return max(dp[n - 2], answer)

# 主函数
if __name__ == '__main__':
    nums = [2,3,2,3]
    s = Solution()
    print("Input: nums = ", nums)
    print("Output: ", s.houseRobber(nums))


# 运行结果
# Input: nums =  [2, 3, 2, 3]
# Output:  6