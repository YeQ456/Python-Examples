# 问题描述
# 给定一个整数数组，其中1 <= a[i] <= n(n为数组的大小)，一些元素出现两次，其他元素出现一次。找到
# [1,n]中所有未出现在此数组中的元素


# 示例
# 输入：[4,3,2,7,8,2,3,1]
# 输出：[5,6]


# 源码实现
class Solution:
    def findDisappearedNumbers(self, nums):
        n = len(nums)
        s = set(nums)
        res = [i for i in range(1, n + 1) if i not in s]
        return res
    
# 主函数
if __name__ == '__main__':
    solution = Solution()
    num = [4,3,2,7,8,2,3,1]
    print("Input: ", num)
    print("Output: ", solution.findDisappearedNumbers(num))



# 运行结果
# Input:  [4, 3, 2, 7, 8, 2, 3, 1]
# Output:  [5, 6]