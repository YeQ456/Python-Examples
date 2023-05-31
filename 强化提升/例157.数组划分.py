# 问题描述
# 将一个没有排序的整数数组划分为3部分：第1部分中所有的值都小于low；第2部分中所有的值都大于或等于low,
# 小于或等于high; 第3部分中所有的值都大于high。返回任意一种可能的情况。在所有测试中都有low <= high


# 示例
# 输入：[4,3,4,1,2,3,1,2], m = 2, n = 3
# 输出：[1,1,2,3,2,3,4,4]

# 输入：[3,2,1], m = 2, n = 3
# 输出：[1,2,3]


# 源码实现
class Solution:
    def partition(self, nums, low, high):
        if len(nums) <= 1:
            return
        pl,pr = 0,len(nums) - 1
        i = 0
        while i <= pr:
            if nums[i] < low:
                nums[pl], nums[pr] = nums[i], nums[pl]
                pl += 1
                i += 1
            elif nums[i] > high:
                nums[pr], nums[i] = nums[i], nums[pr]
                pr -= 1
            else:
                i += 1
        return nums

# 主函数
if __name__ == '__main__':
    nums = [4,3,4,1,2,3,1,2]
    low = 2
    high = 3
    s = Solution()
    print("Input: nums = ", nums, ", low = ",low, ", high = ", high)
    print("Output: ", s.partition(nums,low,high))


# 运行结果
# Input: nums =  [4, 3, 4, 1, 2, 3, 1, 2] , low =  2 , high =  3
# Output:  [1, 1, 1, 1, 2, 3, 4, 4]