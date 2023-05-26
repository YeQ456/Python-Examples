# 问题描述
# 在n个数组中找到第k大元素


# 示例
# 输入：k = 3, [[9,3,2,4,7],[1,2,3,4,8]]
# 输出：7

# 输入：k = 2, [[9,3,2,4,8],[1,2,3,4,2]]
# 输出：8


# 源码实现
import heapq
class Solution:
    def KthInArrays(self, arrays, k):
        if not arrays:
            return None
        sortedArrays = []
        for arr in arrays:
            if not arr:
                continue
            sortedArrays.append(sorted(arr, reverse=True))
        maxheap = [(-arr[0],index,0) for index, arr in enumerate(sortedArrays)]
        heapq.heapify(maxheap)
        num = None
        for i in range(k):
            num, x, y = heapq.heappop(maxheap)
            num = -num
            if y + 1 < len(sortedArrays[x]):
                heapq.heappush(maxheap, (-sortedArrays[x][y + 1], x, y + 1))
        return num

# 主函数
if __name__ == '__main__':
    nums = [[2,3,2,4],[3,4,7,9]]
    k = 5
    s = Solution()
    print("Input: nums = ", nums, ", k = ", k)
    print("Output: ", s.KthInArrays(nums,k))


# 运行结果
# Input: nums =  [[2, 3, 2, 4], [3, 4, 7, 9]] , k =  5
# Output:  3