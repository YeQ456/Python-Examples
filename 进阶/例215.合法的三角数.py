# 问题描述
# 给定一个包含非负整数的数组，用从数组中选出的可以制作三角形的三元组数目作为三角形的边长


# 示例
# 输入：[2,2,3,4]
# 输出：3
# 解释：合法的组合为[2,3,4](使用第1个2)、[2,3,4](使用第2个2)、[2,2,3]


# 源码实现
class Solution:
    def triangleNumber(self, nums):
        nums = sorted(nums)
        total = 0
        for i in range(len(nums) - 2):
            if nums[i] == 0:
                continue
            end = i + 2
            for j in range(i + 1, len(nums) - 1):
                while end < len(nums) and nums[end] < (nums[i] + nums[j]):
                    end += 1
                total += end - j - 1
        return total

if __name__ == '__main__':
    s = Solution()
    nums = [2,2,3,4]
    print("输入：", nums)
    print("输出：", s.triangleNumber(nums))


# 运行结果
# 输入： [2, 2, 3, 4]
# 输出： 3