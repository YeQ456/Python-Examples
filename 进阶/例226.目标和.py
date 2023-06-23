# 问题描述
# 给定一个非负整数的列表a1, a2, ... , an，再给定一个目标S。用+和-两种运算符号，对于每一个整数，选择一个
# 作为其前面的符号。找出有多少种方法可以使得这些整数的和正好等于S


# 示例
# 输入：nums = [1,1,1,1,1], S = 3
# 输出：5
# 解释：
# 第一种：-1 + 1 + 1 + 1 + 1 = 3
# 第二种：+1 - 1 + 1 + 1 + 1 = 3
# 第三种：+1 + 1 - 1 + 1 + 1 = 3
# 第四种：+1 + 1 + 1 - 1 + 1 = 3
# 第五种：+1 + 1 + 1 + 1 - 1 = 3


# 源码实现
class Solution(object):
    def findTargetSumWays(self, nums, S):
        if not nums:
            return 0
        dic = {nums[0]:1, -nums[0]:1} if nums[0] != 0 else {0:2}
        for i in range(1, len(nums)):
            tdic = {}
            for d in dic:
                tdic[d + nums[i]] = tdic.get(d + nums[i], 0) + dic.get(d, 0)
                tdic[d - nums[i]] = tdic.get(d - nums[i], 0) + dic.get(d, 0)
            dic = tdic
        return dic.get(S, 0)

if __name__ == '__main__':
    s = Solution()
    S = 3
    nums = [1,1,1,1,1]
    print("输入目标值：", S)
    print("输入列表：", nums)
    print("输出方法数：", s.findTargetSumWays(nums, S))


# 运行结果
# 输入目标值： 3
# 输入列表： [1, 1, 1, 1, 1]
# 输出方法数： 5