# 问题描述
# 给定一个大小为n的非空整数数组，找出使得数组中所有元素相同的最小步数。其中一步被定义为将数组中n - 1
# 个元素加1


# 示例
# 输入：[1,2,3]
# 输出：3
# 解释：每一步将其中2个元素加1，[1,2,3]=>[2,3,3]=>[3,4,3]=>[4,4,4]，只需要3步


# 源码实现
class Solution(object):
    def minMoves(self, nums):
        sumNum = sum(nums)
        minNum = min(nums)
        return sumNum - minNum * len(nums)

# 主函数
if __name__ == '__main__':
    s = Solution()
    n = [1,2,3]
    print("Input: ", n)
    print("Output: ", s.minMoves(n))



# 运行结果
# Input:  [1, 2, 3]
# Output:  3