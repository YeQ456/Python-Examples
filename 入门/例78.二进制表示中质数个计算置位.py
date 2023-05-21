# 问题描述
# 计算置位代表二进制形式中1的个数。给定2个整数L和R，找到闭区间[L,R]范围，计算置位位数位质数的整数个数。
# 例如21的二进制形式10101有3个计算置位，3是质数


# 示例
# 输入：L = 6, R = 10
# 输出：4
# 解释：6->0110(2是质数)，7->0111(3是质数)，9->1001(2是质数)，10->1010(2是质数)


# 源码实现
class Solution:
    def countPrimeSetBits(self, L, R):
        k = 0
        for n in range(L, R + 1):
            if bin(n).count('1') in [2,3,5,7,11,13,17,19]:
                k = k + 1
        return k

# 主函数
if __name__ == '__main__':
    solution = Solution()
    L = 6
    R = 10
    print("Input: [", L, ",", R, "]")
    print("Output: ", solution.countPrimeSetBits(L,R))



# 运行结果
# Input: [ 6 , 10 ]
# Output:  4