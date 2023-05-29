# 问题描述
# 给定一个整数数组，找出这个数组中有多少对的和小于或等于目标值，返回符合要求的组合对数


# 示例
# 输入：nums = [2,7,11,15], target = 24
# 输出：5
# 解释：2 + 7 < 24, 2 + 11 < 24, 2 + 15 < 24, 7 + 11 < 24, 7 + 15 < 24，所以符合要求的共5对

# 输入：nums = [1], target = 1
# 输出：0


# 源码实现
class Solution:
    def twoSum(self, nums, target):
        l,r = 0, len(nums) - 1
        cnt = 0
        nums.sort()
        while l < r:
            value = nums[l] + nums[r]
            if value > target:
                r -= 1
            else:
                cnt += r - l
                l += 1
        return cnt

# 主函数
if __name__ == '__main__':
    nums = [2,7,11,15]
    target = 24
    s = Solution()
    print("Input: nums = ", nums, ", target = ", target)
    print("Output: ", s.twoSum(nums, target))


# 运行结果
# Input: nums =  [2, 7, 11, 15] , target =  24
# Output:  5