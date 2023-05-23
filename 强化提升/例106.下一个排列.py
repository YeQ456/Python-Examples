# 问题描述
# 给定一个整数数组表示排列，找出以字典为顺序的下一个排列


# 示例
# 输入：[1,3,2,3]
# 输出：[1,3,3,2]

# 输入：[4,3,2,1]
# 输出：[1,2,3,4]


# 源码实现
class Solution:
    def nextPermutation(self, nums):
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                break
        else:
            nums.reverse()
            return nums
        for j in range(len(nums) - 1, i, -1):
            if nums[j] > nums[i]:
                nums[i], nums[j] = nums[j], nums[i]
                break
        for j in range(0, (len(nums) - i) // 2):
            nums[i + j + 1], nums[len(nums) - j - 1] = nums[len(nums) - j - 1], nums[i + j + 1]
        return nums

# 主函数
if __name__ == '__main__':
    s = Solution()
    num = [1,3,2,3]
    ans = s.nextPermutation(num)
    print("Input: ", num)
    print("Output: ", ans)



# 运行结果
# Input:  [1, 3, 2, 3]
# Output:  [1, 3, 3, 2]