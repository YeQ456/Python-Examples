# 问题描述
# 给定一个整数数组，1 <= a[i] <= n（n为数组的大小），一些元素出现2次，其他元素出现1次，找到在此数组中
# 出现2次的所有元素


# 示例
# 输入：[4,3,2,7,8,2,3,1]
# 输出：[2,3]


# 源码实现
class Solution:
    def findDuplicates(self, nums):
        if not nums:
            return []
        duplicates = []
        for each in range(len(nums)):
            index = nums[each]
            if index < 0:
                index = -index
            if nums[index - 1] > 0:
                nums[index - 1] = -nums[index - 1]
            else:
                duplicates.append(index)
        return duplicates

if __name__ == '__main__':
    s = Solution()
    n = [4,3,2,7,8,2,3,1]
    print("输入：", n)
    print("输出：", s.findDuplicates(n))


# 运行结果
# 输入： [4, 3, 2, 7, 8, 2, 3, 1]
# 输出： [2, 3]