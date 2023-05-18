# 问题描述
# 在一个排序数组中查找目标数，返回该目标数的出现的任一个位置，若不存在，返回-1


# 示例
# 输入：nums = [1,2,2,4,5,5], target = 2
# 输出：1或2

# 输入：nums = [1,2,2,4,5,5], target = 6
# 输出：-1


# 源码实现
class Solution:
    def findPosition(self, nums, target):
        if len(nums) is 0:
            return -1
        
        start = 0
        end = len(nums) - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if nums[mid] == target:
                end = mid
            elif nums[mid] < target:
                start = mid
            else:
                end = mid
        
        if nums[start] == target:
            return start
        if nums[end] == target:
            return end
        
        return -1

# 主函数
if __name__ == '__main__':
    generator = [1,2,2,4,5,5]
    target = 2
    solution = Solution()
    print("Input: nums = ",generator, ", target = ", target)
    print("Output: ", solution.findPosition(generator,target))



# 运行结果
# Input: nums =  [1, 2, 2, 4, 5, 5] , target =  2
# Output:  1