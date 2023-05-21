# 问题描述
# 给定一个整数数组nums，编写一个返回此数组“中心索引”的方法。中心索引左边的数字之和等于右边的数字之和
# 若不存在这样的中心索引，返回-1.若有多个中心索引，则返回最左侧的那一个


# 示例
# 输入：nums = [1,7,3,6,5,6]
# 输出：3
# 解释：索引3(nums[3] = 6)左侧所有数字之和等于右侧数字之和，且3是满足条件的第1个索引


# 源码实现
class Solution(object):
    def pivotIndex(self, nums):
        left, right = 0, sum(nums)
        for index, num in enumerate(nums):
            right -= num
            if left == right:
                return index
            left += num
        return -1

# 主函数
if __name__ == '__main__':
    solution = Solution()
    words = [1,7,3,6,5,6]
    print("Input: nums = ", words)
    print("Output: ", solution.pivotIndex(words))



# 运行结果
# Input: nums =  [1, 7, 3, 6, 5, 6]
# Output:  3