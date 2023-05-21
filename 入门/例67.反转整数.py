# 问题描述
# 将一个整数中的数字进行颠倒，当颠倒后的整数溢出时，返回0(标记为32位整数)


# 示例
# 输入：234
# 输出：432


# 源码实现
class Solution:
    def reverseInteger(self, n):
        if n == 0:
            return 0
        neg = 1
        if n < 0:
            neg, n = -1, -n
        reverse = 0
        while n > 0:
            reverse = reverse * 10 + n % 10
            n = n // 10
        reverse = reverse * neg
        if reverse < -(1 << 31) or reverse > (1 << 31) - 1:
            return 0
        return reverse

# 主函数
if __name__ == '__main__':
    num = 1234
    solution = Solution()
    print("Input: ", num)
    print("Output: ", solution.reverseInteger(num))



# 运行结果
# Input:  1234
# Output:  4321