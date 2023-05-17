# 问题描述
# 给定一个有序的整数数组（升序或降序）和一个待查找的目标整数target，查找到target第1次出现的下标
# （从0开始），若target不存在于数组中，则返回-1


# 示例
# 输入：[1,4,4,5,7,7,8,9,9,10], target = 1
# 输出：0

# 输入：[1,2,3,3,4,5,10], target = 3
# 输出：2

# 输入：[1,2,3,3,4,5,10], target = 6
# 输出：-1


# 源码实现
class Solution:
    def search(self, nums, start, end, target):
        if start > end:
            return -1

        mid = (start + end) // 2
        if nums[mid] > target:
            return self.search(nums, start, mid, target)
        if nums[mid] == target:
            return mid
        if nums[mid] < target:
            return self.search(nums, mid, end, target)

    def binarySearch(self, nums, target):
        return self.search(nums, 0, len(nums) - 1, target)

# 主函数
if __name__ == '__main__':
    solution = Solution()
    nums = [1,2,3,4,5,6]
    target = 3
    ans = solution.binarySearch(nums, target)
    print("Input: nums = ", nums, ", ", "target = ", target)
    print("Output: ", ans)



# 运行结果
# Input: nums =  [1, 2, 3, 4, 5, 6] ,  target =  3
# Output:  2