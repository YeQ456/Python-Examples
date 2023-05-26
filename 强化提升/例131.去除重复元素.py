# 问题描述
# 给出一个个整数数组，去除重复的元素。要求在原数组上操作；将去除重复之后的元素放在数组的开头；不需要保持
# 原数组的顺序。返回去除重复元素之后的元素个数


# 示例
# 输入：nums = [1,3,1,4,4,2]
# 输出：4
# 解释：将重复的整数移动到nums的尾部，变成nums = [1,3,4,2,?,?]，返回nums中唯一整数的数量4

# 输入：nums = [1,2,3]
# 输出：3


# 源码实现
class Solution:
    def deduplication(self, nums):
        n = len(nums)
        if n == 0:
            return 0
        nums.sort()
        result = 1
        for i in range(1,n):
            if nums[i - 1] != nums[i]:
                nums[result] = nums[i]
                result += 1
        return result

# 主函数
if __name__ == '__main__':
    nums = [1,3,1,4,4,2]
    s = Solution()
    print("Input: ", nums)
    print("Output: ", s.deduplication(nums))


# 运行结果
# Input:  [1, 3, 1, 4, 4, 2]
# Output:  4