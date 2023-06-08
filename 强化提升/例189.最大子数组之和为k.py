# 问题描述
# 给一个数组nums和目标值k，找到数组中最长的子数组，使其中的元素和为k。若没有，则返回0


# 示例
# 输入：nums = [1,-1,5,-2,3], k = 3
# 输出：4
# 解释：因为子数组[1,-1,5,-2]的和为3，且长度最大

# 输入：nums = [-2,-1,2,1], k = 1
# 输出：2
# 解释：因为子数组[-1,2]的和为1，且长度最大


# 源码实现
class Solution:
    def maxSubArrayLen(self, nums, k):
        m = {}
        ans = 0
        m[k] = 0
        n = len(nums)
        sum = [0 for i in range(n + 1)]
        for i in range(1, n + 1):
            sum[i] = sum[i - 1] + nums[i - 1]
            if sum[i] in m:
                ans = max(ans, i - m[sum[i]])
            if sum[i] + k not in m:
                m[sum[i] + k] = i
        return ans

# 主函数
if __name__ == '__main__':
    nums = [-2,7,3,-4,1]
    k = 5
    s = Solution()
    print("输入：", nums, ", k = ", k)
    print("输出：", s.maxSubArrayLen(nums, k))


# 运行结果
# 输入： [-2, 7, 3, -4, 1] , k =  5
# 输出： 5