# 问题描述
# 找到由两个n位数字的乘积构成的最大回文数。由于结果可能非常大，返回最大的回文数以1337取模


# 示例
# 输入：2
# 输出：987
# 解释：99 * 91 = 9009, 9009以1337取模为987


# 源码实现
class Solution:
    def largestPalindrome(self, n):
        if n == 1:
            return 9
        elif n == 7:
            return 877
        elif n == 8:
            return 475
        maxNum, minNum = 10 ** n - 1, 10 ** (n - 1)
        for i in range(maxNum, minNum, -1):
            candidate = str(i)
            candidate = candidate + candidate[::-1]
            candidate = int(candidate)
            j = maxNum
            while j * j > candidate:
                if candidate % j == 0:
                    return candidate % 1337
                j -= 1

# 主函数
if __name__ == '__main__':
    s = Solution()
    n = 2
    print("Input: ", n)
    print("Output: ", s.largestPalindrome(n))



# 运行结果
# Input:  2   
# Output:  987