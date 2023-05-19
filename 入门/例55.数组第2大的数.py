# 问题描述
# 在一个数组中找到第2大的数


# 示例
# 输入：[1,3,2,4]
# 输出：3
# 解释：数组中第2大的数是3

# 输入：[1,2]
# 输出：1


# 源码实现
class Solution:
    def seconfMax(self, nums):
        maxValue = max(nums[0], nums[1])
        secValue = min(nums[0], nums[1])
        for i in range(2, len(nums)):
            if nums[i] > maxValue:
                secValue = maxValue
                maxValue = nums[i]
            elif nums[i] > secValue:
                secValue = nums[i]
        
        return secValue

# 主函数
if __name__ == '__main__':
    nums = [3,4,7,9]
    solution = Solution()
    print("Input: ", nums)
    print("Output: ", solution.seconfMax(nums))



# 运行结果
# Input:  [3, 4, 7, 9]
# Output:  7