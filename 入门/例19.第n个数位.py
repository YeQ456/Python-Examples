# 问题描述
# 找出无限正整数数列1,2,...中第n个数位


# 示例
# 输入：11
# 输出：0
# 解释：数字序列1,2,...中第11位是0


# 源码实现
class Solution:
    def findNthDigit(self, n):
        length = 1
        count = 9
        start = 1
        while n > length * count:
            # 以此类推，二位数的个数为90，从10开始
            n -= length * count
            length += 1
            count *= 10
            start *= 10
        
        # 找到第n位数所在的整数start
        start += (n - 1) // length
        return int(str(start)[(n - 1) % length])

# 主函数
if __name__ == '__main__':
    solution = Solution()
    n = 11
    print("Input: n = ", n)
    print("Output: ", solution.findNthDigit(n))



# 运行结果
# Input: n =  11
# Output:  0