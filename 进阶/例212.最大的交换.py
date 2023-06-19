# 问题描述
# 给定一个非负整数，可选择交换它的两个数位，返回能获得的最大的合法数


# 示例
# 输入：2736
# 输出：7236
# 解释：交换数字2和7


# 源码实现
class Solution:
    def maximumSwap(self, num):
        res, num = num, list(str(num))
        for i in range(len(num) - 1):
            for j in range(i + 1, len(num)):
                if int(num[j]) > int(num[i]):
                    tmp = int("".join(num[:i] + [num[j]] + num[i+1:j] + [num[i]] + num[j+1:]))
                    res = max(res,tmp)
        return res

if __name__ == '__main__':
    s = Solution()
    num = 2736
    print("输入：", num)
    print("输出：", s.maximumSwap(num))


# 运行结果
# 输入： 2736
# 输出： 7236