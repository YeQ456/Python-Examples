# 问题描述
# 给一个二进制数组，找到0和1数量相等的最大长度


# 示例
# 输入：[0,1]
# 输出：2
# 解释：[0,1]具有相等数量0和1的最长子数组


# 输入：[0,1,0]
# 输出：2
# 解释：[0,1](或[1,0])具有相等数量0和1的最长子数组


# 源码实现
class Solution:
    def findMaxLength(self, nums):
        index_sum = {}
        cur_sum = 0
        ans = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                cur_sum -= 1
            else:
                cur_sum += 1
            if cur_sum == 0:
                ans = i + 1
            elif cur_sum in index_sum:
                ans = max(ans, i - index_sum[cur_sum])
            if cur_sum not in index_sum:
                index_sum[cur_sum] = i
        return ans

if __name__ == '__main__':
    s = Solution()
    nums = [1,0]
    print("输入：", nums)
    print("输出：", s.findMaxLength(nums))


# 运行结果
# 输入： [1, 0]
# 输出： 2  