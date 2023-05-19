# 问题描述
# 有n堆石子排成一列，目标是将所有的石子合并成一堆。合并规则为：每一次可以合并相邻位置的两堆石子；每次
# 合并的代价为所合并的两堆石子的重量之和；求出最小的合并代价


# 示例
# 输入：[3,4,3]
# 输出：17
# 解释：合并第1堆和第2堆 => [7,3], score = 7; 合并两堆 => [10], score = 17

# 输入：[4,1,1,4]
# 输出：18
# 解释：合并第2堆和第3堆 => [4,2,4], score = 2, 合并前两堆 => [6,4], score = 8; 合并剩余两堆 => [10], score = 18


# 源码实现
import sys
class Solution:
    def stoneGame(self, A):
        n = len(A)
        if n < 2:
            return 0
        dp = [[0] * n for i in range(n)]
        cut = [[0] * n for i in range(n)]
        range_sum = self.get_range_sum(A)
        for i in range(n - 1):
            dp[i][i + 1] = A[i] + A[i + 1]
            cut[i][i + 1] = i
        

        for length in range(3, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                dp[i][j] = sys.maxsize
                for mid in range(cut[i][j - 1], cut[i + 1][j] + 1):
                    if dp[i][j] > dp[i][mid] + dp[mid + 1][j] + range_sum[i][j]:
                        dp[i][j] = dp[i][mid] + dp[mid + 1][j] + range_sum[i][j]
                        cut[i][j] = mid
        
        return dp[0][n - 1]
    
    def get_range_sum(self, A):
        n = len(A)
        range_sum = [[0] * n for i in range(len(A))]
        for i in range(n):
            range_sum[i][i] = A[i]
            for j in range(i + 1, n):
                range_sum[i][j] = range_sum[i][j - 1] + A[j]
        
        return range_sum

# 主函数
if __name__ == '__main__':
    nums = [3,4,3]
    solution = Solution()
    print("Input: ", nums)
    print("Output: ", solution.stoneGame(nums))



# 运行结果
# Input:  [3, 4, 3]
# Output:  17