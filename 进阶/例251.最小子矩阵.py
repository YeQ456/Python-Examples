# 问题描述
# 给定一个大小为n X m的矩阵arr，矩阵的每个位置有一个可正可负的整数，要求从矩阵中取出一个非空子矩阵，使其包含的数字之和最小，输出最小子矩阵的数字和。


# 示例
# 输入： a = [[-3, -2, -1], [-2, 3, -2], [-1, 3, -1]]
# 输出：-7

# 输入：a = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
# 输出：1


# 源码实现
class Solution:
  def minimumSubmatrix(self, arr):
    ans = arr[0][0]
    for i in range(len(arr)):
      sum = [0 for x in range(len(arr[0]))]
      for j in range(i, len(arr)):
        for k in range(len(arr[0])):
          sum[k] += arr[j][k]
          dp = [0 for i in range(len(arr[0]))]
          for k in range(len(arr[0])):
            if k == 0:
              dp[k] = sum[k]
            else:
              dp[k] = min(sum[k], dp[k - 1] + sum[k])
            ans = min(ans, dp[k])
    return ans

if __name__ == '__main__':
  arr = a = a = [[-3, -2, -1], [-2, 3, -2], [-1, 3, -1]]
  s = Solution()
  print("矩阵：", arr)
  print("最小子矩阵：", s.minimumSubmatrix(arr))


# 运行结果
# 矩阵：a = [[-3, -2, -1], [-2, 3, -2], [-1, 3, -1]]
# 最小子矩阵：-7
