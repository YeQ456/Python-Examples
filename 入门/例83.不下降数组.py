# 问题描述
# 一个数组中，若array[i] <= array[i + 1]对于每一个i(1 <= i < n)都成立则该数组是不下降的。给定一个
# 包含n个整数的数组，检测在改变至多1个元素的情况下，它是否可以变成不下降的


# 示例
# 输入：[4,2,3]
# 输出：True
# 解释：因为可以把第一个4修改为1，从而得到一个不下降数组

# 输入：[4,2,1]
# 输出：False
# 解释：因为在修改至多1个元素的情况下，无法得到一个不下降数组


# 源码实现
class Solution:
    def checkPossibility(self, nums):
        count = 0
        for i in range(1, len(nums)):
            if nums[i] < nums[i - 1]:
                count += 1
                if i >= 2 and nums[i] < nums[i - 2]:
                    nums[i] = nums[i - 1]
                else:
                    nums[i - 1] = nums[i]
        return count <= 1

# 主函数
if __name__ == '__main__':
    solution = Solution()
    nums = [4,2,3]
    print("Input: nums = ", nums)
    print("Output: ", solution.checkPossibility(nums))



# 运行结果
# Input: nums =  [4, 2, 3]
# Output:  True