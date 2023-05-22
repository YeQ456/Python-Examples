# 问题描述
# 给出一个含有重复数字的列表，找出列表所有的排列


# 示例
# 输入：[1,1]
# 输出：[[1,1]]

# 输入：[1,2,2]
# 输出：[[1,2,2],[2,1,2],[2,2,1]]


# 源码实现
class Solution:
    def permuteUnique(self, nums):
        def _permute(result, temp, nums):
            if nums == []:
                result += [temp]
            else:
                for i in range(len(nums)):
                    if i > 0 and nums[i] == nums[i - 1]:
                        continue
                    _permute(result, temp + [nums[i]], nums[:i] + nums[i + 1:])
        if nums is None:
            return []
        if len(nums) == 0:
            return [[]]
        result = []
        _permute(result, [], sorted(nums))
        return result

# 主函数
if __name__ == '__main__':
    s = Solution()
    nums = [1,2,2]
    ans = s.permuteUnique(nums)
    print("Input: ", nums)
    print("Output: ", ans)



# 运行结果
# Input:  [1, 2, 2]
# Output:  [[1, 2, 2], [2, 1, 2], [2, 2, 1]]