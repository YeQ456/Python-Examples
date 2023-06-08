# 问题描述
# 给出一个非负整数num，对所有满足0 <= i <= num条件的数字，计算其二进制表示中数字1的个数，并以数组
# 的形式返回


# 示例
# 输入：5
# 输出：[0,1,1,2,1,2]
# 解释：0-5的二进制表示分别是000、001、010、011、100、101，每个数字中1的个数分别为0、1、1、2、1、2

# 输入：3
# 输出：[0,1,1,2]


# 源码实现
class Solution:
    def countBits(self, num):
        f = [0] * (num + 1)
        for i in range(1, num + 1):
            f[i] = f[i & i - 1] + 1
        return f

# 主函数
if __name__ == '__main__':
    num = 5
    s = Solution()
    print("Input: ", num)
    print("Output: ", s.countBits(num))


# 运行结果
# Input:  5
# Output:  [0, 1, 1, 2, 1, 2]