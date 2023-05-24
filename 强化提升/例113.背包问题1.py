# 问题描述
# 有n个物品的体积A[i]及其价值V[i], 将它们装入一个大小为m的背包，最多能装入物品的总价值为多少？


# 示例
# 对于物品体积[2,3,5,7]和对应的价值[1,5,2,4]，假设背包体积大小为10，最大能够装入的价值为9，也即是
# 体积为3和7的物品


# 源码实现
class Solution:
    def backPackII(self, m, A, V):
        f = [0 for i in range(m + 1)]
        n = len(A)
        for i in range(n):
            for j in range(m, A[i] - 1, -1):
                f[j] = max(f[j], f[j - A[i]] + V[i])
        return f[m]

# 主函数
if __name__ == '__main__':
    s = Solution()
    m = 100
    A = [77,22,29,50,99]
    V = [92,22,87,46,90]
    result = s.backPackII(m, A, V)
    print("Input:\n","m = ", m, "\n A = ",A, "\n V = ",V)
    print("Output: ", result)



# 运行结果
# Input:
#  m =  100 
#  A =  [77, 22, 29, 50, 99]
#  V =  [92, 22, 87, 46, 90]
# Output:  133