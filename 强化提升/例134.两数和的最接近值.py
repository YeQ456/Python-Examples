# 问题描述
# 给定数组，找到2个数字，使得它们的和最接近target，返回target与两数之和的差


# 示例
# 输入：nums = [-1,2,1,-4]，target = 4
# 输出：1
# 解释：4 - (2 + 1) = 1，所以最小差距为1

# 输入：nums = [-1,-1,-1,-4], target = 4
# 输出：6
# 解释：4 - (-1-1) = 6，所以最小差距为6


# 源码实现
import sys
class Solution:
    def twoSumClosest(self, nums, target):
        nums.sort()
        i, j = 0, len(nums) - 1
        diff = sys.maxsize
        while i < j:
            if nums[i] + nums[j] < target:
                diff = min(diff, target - nums[i] - nums[j])
                i += 1
            else:
                diff = min(diff, nums[i] + nums[j] - target)
                j -= 1
        return diff

# 主函数
if __name__ == '__main__':
    num = [-1,2,-1,4]
    s = Solution()
    target = 4
    print("Input: nums = ", num, ", target = ", target)
    print("Output: ", s.twoSumClosest(num, target))


# 运行结果
# Input: nums =  [-1, 2, -1, 4] , target =  4
# Output:  1