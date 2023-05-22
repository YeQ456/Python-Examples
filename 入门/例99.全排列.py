# 问题描述
# 给定一个数字列表，返回其所有可能的排列


# 示例
# 输入：[1]
# 输出：[[1]]

# 输入：[1,2,3]
# 输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]


# 源码实现
class Solution:
    def permute(self, nums):
        def _permute(result, temp, nums):
            if nums == []:
                result += [temp]
            else:
                for i in range(len(nums)):
                    _permute(result, temp + [nums[i]], nums[:i] + nums[i + 1:])
        if nums is None:
            return []
        if nums is []:
            return [[]]
        result = []
        _permute(result, [], sorted(nums))
        return result

# 主函数
if __name__ == '__main__':
    nums = [1,2,3]
    s = Solution()
    ans = s.permute(nums)
    print("Input: ", nums)
    print("Output: ", ans)



# 运行结果
# Input:  [1, 2, 3]
# Output:  [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]