# 问题描述
# 给定两个字符串A和B，找到A必须重复的最小次数，使得B是它的子字符串。若没有这样的解决方案，返回-1


# 示例
# 输入：A = "abcd", B = "cdabcdab"
# 输出：3
# 解释：A重复3次为"abcdabcdabcd"，B将成为它的一个子串，若A只重复2次("abcdabcd")，B并非是它的一个子串


# 源码实现
class Solution:
    def repeatedStringMatch(self, A, B):
        C = ""
        for i in range(int(len(B) / len(A) + 3)):
            if B in C:
                return i
            C += A
        return -1

# 主函数
if __name__ == '__main__':
    solution = Solution()
    A = "abcd"
    B = "cdabcdab"
    print("Input: A = ", A, ", B = ", B)
    print("Output: ", solution.repeatedStringMatch(A, B))



# 运行结果
# Input: A =  abcd , B =  cdabcdab
# Output:  3