# 问题描述
# 给出两个字符串，找到最长公共子串，并返回其长度


# 示例
# 输入："ABCD"和"CBCE"
# 输出：2
# 解释：最长公共子串"BC"

# 输入："ABCD"和"EACB"
# 输出：1
# 解释：最长公共子串'A'或'B'或'C'


# 源码实现
class Solution:
    def longestCommonSubstring(self, A, B):
        ans = 0
        for i in range(len(A)):
            for j in range(len(B)):
                l = 0
                while (i + l) < len(A) and (j + l) < len(B) and A[i + l] == B[j + l]:
                    l += 1
                if l > ans:
                    ans = 1
        return ans

# 主函数
if __name__ == '__main__':
    s = Solution()
    A = "ABCD"
    B = "CBCE"
    ans = s.longestCommonSubstring(A, B)
    print("Input: A = ",A, ", B = ", B)
    print("Output: ", ans)



# 运行结果
# Input: A =  ABCD , B =  CBCE
# Output:  1