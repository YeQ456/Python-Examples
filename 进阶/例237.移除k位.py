# 问题描述
# 给定一个以字符串表示的非负整数，从该数字中移除k个数位，使剩余数位组成的数字尽可能小，求可能的最小结果


# 示例
# 输入：num = "1432219", k = 3
# 输出：1219
# 解释：移除数位4,3,2后生成的最小的新数字为1219


# 源码实现
class Solution:
    def removeKdigits(self, num, k):
        if k == 0:
            return num
        if k >= len(num):
            return "0"
        result_list = []
        for i in range(len(num)):
            while len(result_list) > 0 and k > 0 and result_list[-1] > num[i]:
                result_list.pop()
                k -= 1
            if num[i] != '0' or len(result_list) > 0:
                result_list.append(num[i])
        while len(result_list) > 0 and k > 0:
            result_list.pop()
            k -= 1
        if len(result_list) == 0:
            return '0'
        return ''.join(result_list)

if __name__ == '__main__':
    s = Solution()
    n = "1432219"
    k = 3
    print("输入数字：", n)
    print("输入移除数：", k)
    print("输出：", s.removeKdigits(n, k))


# 运行结果
# 输入数字： 1432219
# 输入移除数： 3
# 输出： 1219