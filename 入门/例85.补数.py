# 问题描述
# 给定一个正整数，输出它的补数。补数：将原数字的二进制形式按位取反，再转回十进制后得到的新数


# 示例
# 输入：5
# 输出：2
# 解释：5的二进制形式为101，补数为010，则输出2


# 源码实现
class Solution:
    def findComplement(self, num):
        return num ^ ((1 << num.bit_length()) - 1)

# 主函数
if __name__ == '__main__':
    s = Solution()
    n = 5
    print("Input: ", n)
    print("Output: ", s.findComplement(n))



# 运行结果
# Input:  5
# Output:  2