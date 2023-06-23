# 问题描述
# 给定一个整数数组，找到所有可能的升序子序列。一个升序子序列的长度至少应该为2


# 示例
# 输入：[4,6,7,7]
# 输出：[[4,6],[4,6,7],[4,6,7,7],[4,7],[4,7,7],[6,7],[6,7,7],[7,7]]


# 源码实现
class Solution(object):
    def findSubsequences(self, nums):
        res = []
        self.subsets(nums, 0, [], res)
        return res

    def subsets(self, nums, index, temp, res):
        if len(nums) >= index and len(temp) >= 2:
            res.append(temp[:])
        used = {}
        for i in range(index, len(nums)):
            if len(temp) > 0 and temp[-1] > nums[i]:
                continue
            if nums[i] in used:
                continue
            used[nums[i]] = True
            temp.append(nums[i])
            self.subsets(nums, i + 1, temp, res)
            temp.pop()

if __name__ == '__main__':
    s = Solution()
    nums = [4,6,7,7]
    print("输入：", nums)
    print("输出：", s.findSubsequences(nums))


# 运行结果
# 输入： [4, 6, 7, 7]
# 输出： [[4, 6], [4, 6, 7], [4, 6, 7, 7], [4, 7], [4, 7, 7], [6, 7], [6, 7, 7], [7, 7]]