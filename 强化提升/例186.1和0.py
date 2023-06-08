# 问题描述
# 给定一个只包含0和1的字符串数组，只具有m个0和n个1，找到能由m个0和n个1构成的字符串数组中字符串
# 的最大个数，每一个0和1均只能使用一次


# 示例
# 输入：["10","0001","111001","1","0"], m = 5, n = 3
# 输出：4
# 解释：一共4个字符串，可以用5个0和3个1构成，有："10", "0001", "1", "0"

# 输入：["10","0001","111001","1","0"], m = 7, n = 7
# 输出：5


# 源码实现
class Solution:
    def findMaxForm(self, strs, m, n):
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        for s in strs:
            zero = 0
            one = 0
            for ch in s:
                if ch == "1":
                    one += 1
                else:
                    zero += 1
            for i in range(n, one - 1, -1):
                for j in range(m, zero - 1, -1):
                    if dp[i - one][j - zero] + 1 > dp[i][j]:
                        dp[i][j] = dp[i - one][j - zero] + 1
        return dp[-1][-1]

# 主函数
if __name__ == '__main__':
    nums = ["10","0001","111001","1","0"]
    m = 5
    n = 3
    s = Solution()
    print("输入：", nums, ", m = ", m, ", n = ", n)
    print("输出：", s.findMaxForm(nums, m, n))


# 运行结果
# 输入： ['10', '0001', '111001', '1', '0'] , m =  5 , n =  3
# 输出： 4