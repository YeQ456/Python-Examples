# 问题描述
# 格雷编码是一个二进制数字系统。在该系统中，2个连续的数值仅有1个二进制数字的差异。给定一个非负整数
# n，表示该代码中所有二进制的位数，找出其格雷编码顺序。一个格雷编码顺序必须从0开始，并覆盖所有2^n个
# 整数


# 示例
# 输入：2
# 输出：[0,1,3,2]
# 解释：这几个数字的二进制格雷编码为：
# 0 - 00
# 1 - 01
# 3 - 11
# 2 - 10


# 源码实现
class Solution:
    def grayCode(self, n):
        if n == 0:
            return [0]
        result = self.grayCode(n - 1)
        seq = list(result)
        for i in reversed(result):
            seq.append((1 << (n - 1)) | i)
        return seq

# 主函数
if __name__ == '__main__':
    n = 2
    s = Solution()
    print("Input: ", n)
    print("Output: ", s.grayCode(n))


# 运行结果
# Input:  2
# Output:  [0, 1, 3, 2]