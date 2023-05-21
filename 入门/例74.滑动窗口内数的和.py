# 问题描述
# 给定一个大小为n的整数数组合一个大小为k的滑动窗口，将滑动窗口从头移动到尾，每次移动一个整数输出从
# 开始到结束每个时刻滑动窗口内数的和


# 示例
# 输入：array = [1,2,7,8,5], k = 3
# 输出：[10,17,20]
# 解释：第1个窗口1 + 2 + 7 = 10，第2个窗口2 + 7 + 8 = 17，第3个窗口7 + 8 + 5 = 20


# 源码实现
class Solution:
    def winSum(self, nums, k):
        n = len(nums)
        if n < k or k <= 0:
            return []
        sums = [0] * (n - k + 1)
        for i in range(k):
            sums[0] += nums[i]
        for i in range(1, n - k + 1):
            sums[i] = sums[i - 1] - nums[i - 1] + nums[i + k - 1]
        return sums

# 主函数
if __name__ == '__main__':
    nums = [1,2,7,8,5]
    k = 3
    print("Input: nums = ", nums, ", k = ", k)
    print("Output: ", Solution().winSum(nums, k))



# 运行结果
# Input: nums =  [1, 2, 7, 8, 5] , k =  3
# Output:  [10, 17, 20]