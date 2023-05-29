# 问题描述
# 给定一个整数数组，找到差值等于目标值的2个数。数组的前1个下标index1必须小于第2个下标index2.返回index1
# 和index2所在的索引位置。数组的元素从1开始计数


# 示例
# 输入：nums = [2,7,15,24], target = 5
# 输出：[1,2]

# 输入：nums = [1,1], target = 0
# 输出：[1,2]


# 源码实现
class Solution:
    def twoSub(self, nums, target):
        nums = [(num, i) for i, num in enumerate(nums)]
        target = abs(target)
        n, indexs = len(nums), []
        nums = sorted(nums, key=lambda x : x[0])
        j = 0
        for i in range(n):
            if i == j:
                j += 1
            while j < n and nums[j][0] - nums[i][0] < target:
                j += 1
            if j < n and nums[j][0] - nums[i][0] == target:
                indexs = [nums[i][1] + 1, nums[j][1] + 1]
        if indexs[0] > indexs[1]:
            indexs[0], indexs[1] = indexs[1], indexs[0]
        return indexs

# 主函数
if __name__ == '__main__':
    nums = [2,7,15,24]
    target = 5
    s = Solution()
    print("Input: nums = ", nums, ", target = ", target)
    print("Output: ", s.twoSub(nums, target))


# 运行结果
# Input: nums =  [2, 7, 15, 24] , target =  5
# Output:  [1, 2]