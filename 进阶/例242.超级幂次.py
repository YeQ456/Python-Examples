# # 问题描述
# 计算a^b取模337。其中a是一个正整数，b也是一个正整数，以数组的形式给出


# 示例
# 输入a = 2, b = [3]
# 输出：8


# 源码实现
class Solution:
    def superPow(self, a, b):
        if a == 0:
            return 0
        ans = 1
        def mod(x):
            return x % 1337
        for num in b:
            ans = mod(mod(ans ** 10) * mod(a ** num))
        return ans

if __name__ == '__main__':
    s = Solution()
    n = 2
    k = [3]
    print("输入 a = ", n)
    print("输入 b = ", k)
    print("输出：", s.superPow(n, k))


# 运行结果
# 输入 a =  2
# 输入 b =  [3]
# 输出： 8