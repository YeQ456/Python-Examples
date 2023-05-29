# 问题描述
# 给定数组，找到数组中第k大的元素


# 示例
# 输入：[9,3,2,4,8], k = 3
# 输出：4

# 输入：[1,2,3,4,5,6,8,9,10,7], k = 10
# 输出：1


# 源码实现
class Solution:
    def kthLargestElement(self, nums, k):
        import heapq
        heap = []
        for num in nums:
            heapq.heappush(heap, num)
            if len(heap) > k:
                heapq.heappop(heap)
        return heapq.heappop(heap)

# 主函数
if __name__ == '__main__':
    nums = [9,3,2,4,8]
    k = 3
    s = Solution()
    print("Input: ", nums,", k = ", k)
    print("Output: ", s.kthLargestElement(nums, k))


# 运行结果
# Input:  [9, 3, 2, 4, 8] , k =  3
# Output:  4