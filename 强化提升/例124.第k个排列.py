# 问题描述
# 给定n和k，求n的全排列中字典序第k个排列


# 示例
# 输入：n = 3, k = 4
# 输出：231
# 即n = 3时，按照字典顺序的全排列如下：123、132、213、231、312、321,第4个排列是231


# 源码实现
class Solution:
    def getPermutation(self, n, k):
        fac = [1]
        for i in range(1, n + 1):
            fac.append(fac[-1] * i)
        elegible = list(range(1, n + 1))
        per = []
        for i in range(n):
            digit = (k - 1) // fac[n - i - 1]
            per.append(elegible[digit])
            elegible.remove(elegible[digit])
            k = (k - 1) % fac[n - i - 1] + 1
        return "".join([str(x) for x in per])

# 主函数
if __name__ == '__main__':
    n = 3
    k = 4
    s = Solution()
    print("Input: n = ", n, ", k = ", k)
    print("Output: ", s.getPermutation(n, k))



# 运行结果
# Input: n =  3 , k =  4
# Output:  231