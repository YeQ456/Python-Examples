# 问题描述
# 有n枚硬币，摆放成阶梯形状，即第k行恰好有k枚硬币。给出n，找到可以形成的完整楼梯行数，n为一个非负整数
# 且在32位有符号整数范围内


# 示例
# 样例1：
# 输入：n = 5
#    *
#    *  *
#    *  *
# 输出：2
# 解释：第3行不完整

# 样例2：
# 输入：n = 8
#    *
#    *  *
#    *  *  *
#    *  *  
# 输出：3
# 解释：第4行不完整


# 源码实现
import math
class Solution:
    def arrangeCoins(self, n):
        # n = (1 + x) * x / 2，得到x = (-1 + sqrt(8 * n + 1)) / 2，对x取整
        return math.floor((-1 + math.sqrt(1 + 8 * n)) / 2)

# 主函数
if __name__ == '__main__':
    n = 10
    solution = Solution()
    print("Input: n = ", n)
    print("Output: ", solution.arrangeCoins(n))



# 运行结果
# Input: n =  10
# Output:  4