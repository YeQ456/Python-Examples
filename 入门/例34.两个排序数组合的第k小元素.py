# 问题描述
# 给定两个有序数组A和B，定义集合sum = a + b，其中a来自数组A，b来自数组B，求sum中第k小的元素


# 示例
# 输入：A = [1,7,11], B = [2,4,6]
# 输出：sum = [3,5,7,9,11,13,13,15,17]
# 解释：当k = 3, 返回7；当k = 4,返回9；当k = 8, 返回15


# 源码实现
class Solution:
    def kthSmallestSum(self, A, B, k):
        if not A or not B:
            return None
        
        import heapq
        n, m = len(A), len(B)
        minheap = [(A[0] + B[0], 0, 0)]
        visited = set([0])
        num = None
        for i in range(k):
            num, x, y = heapq.heappop(minheap)
            if x  + 1 < n and (x + 1) * m + y not in visited:
                heapq.heappush(minheap, (A[x + 1] + B[y], x + 1, y))
                visited.add((x + 1) * m + y)
            if y + 1 < m and x * m + y + 1 not in visited:
                heapq.heappush(minheap, (A[x] + B[y + 1], x, y + 1))
                visited.add(x * m + y + 1)
        
        return num

# 主函数
if __name__ == '__main__':
    generator_A = [1,7,11]
    generator_B = [2,4,6]
    k = 4
    solution = Solution()
    print("Input: A = ", generator_A, ", B = ", generator_B, ", k = ", k)
    print("Output: ", solution.kthSmallestSum(generator_A, generator_B, k))



# 运行结果
# Input: A =  [1, 7, 11] , B =  [2, 4, 6] , k =  4
# Output:  9