# 问题描述
# 2个整数之间的汉明距离是相应二进制数位上不同的个数。找到所有给定数字对之间的总汉明距离


# 示例
# 输入：[4,14,2]
# 输出：6
# 解释：二进制中，4是0100,14是1110,2是0010，汉明距离(4,14) + 汉明距离(4,2) + 汉明距离(14,2)
# = 2 + 2 + 2 = 6


# 源码实现
class Solution:
    def totalHammingDistance(self, nums):
        return sum(b.count('0') * b.count('1') for b in zip(*map('{:032b}'.format, nums)))

# 主函数
if __name__ == '__main__':
    solution = Solution()
    n = [4,14,2]
    print("Input: n = ", n)
    print("Output: ", solution.totalHammingDistance(n))



# 运行结果
# Input: n =  [4, 14, 2]
# Output:  6