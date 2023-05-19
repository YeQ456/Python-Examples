# 问题描述
# 水仙花数是指一个N位正整数(N >= 3)，每位数字的N次幂之和等于它的本身。例如：一个3位的十进制整数153
# 就是一个水仙花数。因为153 = 1³ + 5³ + 3³。一个4位的十进制数1634也是一个水仙花数，因为
# 1634 = 1^4 + 6^4 + 3^4 + 4^4。给出N，寻找出所有的N位十进制水仙花数


# 示例
# 输入：1
# 输出：[0,1,2,3,4,5,6,7,8,9]

# 输入：2
# 输出：[]
# 解释：没有2位数字的水仙花数


# 源码实现
class Solution:
    def getNarcissisticNumbers(self, n):
        res = []
        for x in range([0, 10 ** (n - 1)][n > 1], 10 ** n):
            y, k = x, 0
            while x > 0:
                k += (x % 10) ** n
                x //= 10
            if k == y:
                res.append(k)
        
        return res

# 主函数
if __name__ == '__main__':
    solution = Solution()
    n = 4
    ans = solution.getNarcissisticNumbers(n)
    print("Input: n = ", n)
    print("Output: ", ans)



# 运行结果
# Input: n =  4
# Output:  [1634, 8208, 9474]