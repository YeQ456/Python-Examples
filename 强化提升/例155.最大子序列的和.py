# 问题描述
# 给定一个整数数组，找到长度大于或等于k的连续子序列使它们的和最大，返回这个最大的和。若数组中少于k个
# 元素，则返回0


# 示例
# 输入：[-2,2,-3,4,-1,2,1,-5,3], k = 5
# 输出：sum = 5
# 解释：子序列为：[2,-3,4,-1,2,1]

# 输入：[5,-10,4], k = 2
# 输出：sum = -1


# 源码实现
class Solution:
    def maxSubarray(self, nums, k):
        n = len(nums)
        if n < k:
            return 0
        result = 0
        for i in range(k):
            result += nums[i]
        sum = [0 for i in range(n + 1)]
        min_prefix = 0
        for i in range(1, n + 1):
            sum[i] = sum[i - 1] + nums[i - 1]
            if i >= k and sum[i] - min_prefix > result:
                result = max(result, sum[i] - min_prefix)
            if i >= k:
                min_prefix = min(min_prefix, sum[i - k + 1])
        return result

# 主函数
if __name__ == '__main__':
    nums = [-2,2,-3,4,-1,2,1,-5,3]
    k = 5
    s = Solution()
    print("Input: nums = ", nums, ", k = ", k)
    print("Output: sum = ", s.maxSubarray(nums, k))


# 运行结果
# Input: nums =  [-2, 2, -3, 4, -1, 2, 1, -5, 3] , k =  5
# Output: sum =  5