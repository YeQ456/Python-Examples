# 问题描述
# 给定2个数组，求它们的点积


# 示例
# 输入：A = [1,1,1], B = [2,2,2]
# 输出：6
# 解释：1*2 + 1*2 + 1*2 = 6

# 输入：A = [3,2], B = [2,3,3]
# 输出：-1
# 解释：没有点积


# 源码实现
class Solution:
    def dotProduct(self, A, B):
        if len(A) == 0 or len(B) == 0 or len(A) != len(B):
            return -1
        
        ans = 0
        for i in range(len(A)):
            ans += A[i] * B[i]
        
        return ans

# 主函数
if __name__ == '__main__':
    A = [1,1,1]
    B = [2,2,2]
    solution = Solution()
    print("Input: A = ", A, ", B = ", B)
    print("Output: ", solution.dotProduct(A,B))



# 运行结果
# Input: A =  [1, 1, 1] , B =  [2, 2, 2]
# Output:  6