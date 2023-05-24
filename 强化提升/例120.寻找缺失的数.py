# 问题描述
# 给出一个包含0~N中N个数的序列，找出0~N中没有出现在序列中的那个数


# 示例
# 输入：[0,1,3]
# 输出：2

# 输入：[1,2,3]
# 输出：0


# 源码实现
class Solution:
    def findMissing(self, nums):
        if not nums:
            return 0
        sum = 0
        for i in nums:
            sum += i
        return int((len(nums) * (len(nums) + 1) / 2)) - sum

# 主函数
if __name__ == '__main__':
    s = Solution()
    nums = [0,1,3]
    ans = s.findMissing(nums)
    print("Input: ", nums)
    print("Output: ", ans)



# 运行结果
# Input:  [0, 1, 3]
# Output:  2