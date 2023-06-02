# 问题描述
# 给出一个包含n + 1个整数的数组nums，数组中整数值在1 ~ n范围内（含边界），保证至少存在1个重复的整数。
# 假设只有1个重复的整数，返回这个重复的数。要求如下：不能修改数组（假设数组只读）；数组中只有1个重复
# 的数，但可能重复超过1次


# 示例
# 输入：nums = [5,5,4,3,2,1]
# 输出：5

# 输入：nums = [5,4,4,3,2,1]
# 输出：4


# 源码实现
class Solution:
    def findDuplicate(self, nums):
        start, end = 1, len(nums) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if self.smaller_than_or_equal_to(nums, mid) > mid:
                end = mid
            else:
                start = mid
        if self.smaller_than_or_equal_to(nums, start) > start:
            return start
        return end
    
    def smaller_than_or_equal_to(self, nums, val):
        count = 0
        for num in nums:
            if num <= val:
                count += 1
        return count

# 主函数
if __name__ == '__main__':
    nums = [5,5,4,3,2,1]
    s = Solution()
    print("Input: ", nums)
    print("Output: ", s.findDuplicate(nums))


# 运行结果
# Input:  [5, 5, 4, 3, 2, 1]
# Output:  5