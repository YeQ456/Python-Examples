# 问题描述
# 在一个数组中找到前k个最大的数


# 示例
# 输入：[3,10,1000,-99,4,100], k = 3
# 输出：[1000,100,10]

# 输入：[8,7,6,5,4,3,2,1], k = 5
# 输出：[8,7,6,5,4]


# 源码实现
import heapq
class Solution:
    def topk(self, nums, k):
        heapq.heapify(nums)
        topk = heapq.nlargest(k, nums)
        topk.sort()
        topk.reverse()
        return topk

# 主函数
if __name__ == '__main__':
    nums = [8,7,6,5,4,3,2,1]
    k = 4
    s = Solution()
    print("Input: nums = ",nums, ", k = ", k)
    print("Output: ", s.topk(nums,k))


# 运行结果
# Input: nums =  [8, 7, 6, 5, 4, 3, 2, 1] , k =  4
# Output:  [8, 7, 6, 5]