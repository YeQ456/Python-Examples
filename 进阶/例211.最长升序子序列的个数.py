# 问题描述
# 给定一个无序的整数序列，找到最长的升序子序列的个数


# 示例
# 输入：[1,3,5,4,7]
# 输出：2
# 解释：找到最长的两个升序子序列为：[1,3,4,7]和[1,3,5,7]


# 源码实现
import collections
class Solution(object):
    def findNumberOfLIS(self, nums):
        ans = [0,0]
        l = len(nums)
        dp = collections.defaultdict(list)
        for i in range(l):
            dp[i] = [1,1]
        for i in range(l):
            for j in range(i):
                if nums[i] > nums[j]:
                    if dp[j][0] + 1 > dp[i][0]:
                        dp[i] = [dp[j][0] + 1, dp[j][1]]
                    elif dp[j][0] + 1 == dp[i][0]:
                        dp[i] = [dp[i][0], dp[i][1] + dp[j][1]]
        for i in dp.keys():
            if dp[i][0] > ans[0]:
                ans = [dp[i][0], dp[i][1]]
            elif dp[i][0] == ans[0]:
                ans = [dp[i][0], ans[1] + dp[i][1]]
        return ans[1]

if __name__ == '__main__':
    s = Solution()
    nums = [1,3,5,4,7]
    print("输入：", nums)
    print("输出：", s.findNumberOfLIS(nums))


# 运行结果
# 输入： [1, 3, 5, 4, 7]
# 输出： 2