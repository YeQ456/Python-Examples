# 问题描述
# 给定一个整型数组，找到主元素，该主元素在数组中的出现次数大于数组元素个数的1/3


# 示例
# 输入：[99,2,99,2,99,3,3]
# 输出：99

# 输入：[1,2,1,2,1,3,3]
# 输出：1


# 源码实现
class Solution:
    def majorityNumber(self, nums):
        nums.sort()
        i = 0; j = 0
        while i <= len(nums):
            j = nums.count(nums[i])
            if j > len(nums) // 3:
                return nums[i]
            i += j
        return

# 主函数
if __name__ == '__main__':
    s = Solution()
    nums = [99,2,99,2,99,3,3]
    n = s.majorityNumber(nums)
    print("Input: ", nums)
    print("Output: ", n)



# 运行结果
# Input:  [2, 2, 3, 3, 99, 99, 99]
# Output:  99