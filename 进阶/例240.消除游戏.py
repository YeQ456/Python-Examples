# 问题描述
# 从1~n的排序整数列表中删除第一个数字，然后从左到右每隔一个数字删除一个，直到列表尾数；重复上一步骤，
# 但这次从右到左，即从剩余的数字中删除最右边的数字和每隔一个数字删除一个。左右交替重复上述步骤，直到
# 剩下一个数字。找到长度为n的列表剩下的最后一个数字


# 示例
# 输入：9
# 输出：6
# 解释：删除后的列表依次如下：
# 1 2 3 4 5 6 7 8 9
# 2 4 6 8
# 2 6
# 6


# 源码实现
class Solution:
    def lastRemaining(self, n):
        return 1 if n == 1 else 2 * (1 + n // 2 - self.lastRemaining(n // 2))

if __name__ == '__main__':
    s = Solution()
    n = 9
    print("输入：", n)
    print("输出：", s.lastRemaining(n))


# 运行结果
# 输入： 9
# 输出： 6