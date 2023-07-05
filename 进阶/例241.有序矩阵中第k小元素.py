# 问题描述
# 给定一个n X n矩阵，每一行和每一列都按照升序排序，找出矩阵中的第k小元素。注意：将所有元素有序排列的第
# k小元素，而非第k个互不相同的元素


# 示例
# 输入：[[1,5,9],[10,11,13],[12,13,15]], k = 8
# 输出：13


# 源码实现
class Solution:
    def kthSmallest(self, matrix, k):
        start = matrix[0][0]
        end = matrix[-1][-1]
        while start + 1 < end:
            mid = start + (end - start) // 2
            if self.get_num_less_equal(matrix, mid) < k:
                start = mid
            else:
                end = mid
        if self.get_num_less_equal(matrix, start) >= k:
            return start
        return end
    
    def get_num_less_equal(self, matrix, mid):
        m = len(matrix)
        n = len(matrix[0])
        i = 0
        j = n - 1
        count = 0
        while i < m and j >= 0:
            if matrix[i][j] <= mid:
                i += 1
                count += j + 1
            else:
                j -= 1
        return count

if __name__ == '__main__':
    s = Solution()
    n = [[1,5,9],[10,11,13],[12,13,15]]
    k = 8
    print("输入数组：", n)
    print("输入顺序：", k)
    print("输出数字：", s.kthSmallest(n, k))


# 运行结果
# 输入数组： [[1, 5, 9], [10, 11, 13], [12, 13, 15]]
# 输入顺序： 8
# 输出数字： 13