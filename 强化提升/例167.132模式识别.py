# 问题描述
# 给定n个整数的序列a1,a2,...,an。设计一个算法来检查序列中是否存在132模式（132模式：对一个子串ai,aj,ak，
# 满足i<j<k和ai<ak<aj）。n小于20000


# 示例
# 输入：nums = [1,2,3,4]
# 输出：False
# 解释：这个序列中没有132模式

# 输入：nums = [3,1,4,2]
# 输出：True
# 解释：存在132模式[1,4,2]


# 源码实现
import sys
class Solution:
    def find132pattern(self, nums):
        stk = [- sys.maxsize]
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] < stk[-1]:
                return True
            else:
                while stk and nums[i] > stk[-1]:
                    v = stk.pop()
                    stk.append(nums[i])
                    stk.append(v)
        return False

# 主函数
if __name__ == '__main__':
    nums = [3,1,4,2]
    s = Solution()
    print("Input: ", nums)
    print("Output: ", s.find132pattern(nums))


# 运行结果
# Input: [3,1,4,2]
# Output: True