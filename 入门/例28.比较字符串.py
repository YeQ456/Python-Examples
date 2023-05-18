# 问题描述
# 比较两个字符串A和B，字符串A和B中的字符都是大写字母，确定A中是否包含B中所有的字符


# 示例
# 输入：A = "ABCD", B = "ACD"
# 输出：True

# 输入：A = "ABCD", B = "AABC"
# 输出：False


# 源码实现
class Solution:
    def compareStrings(self, A, B):
        if len(B) == 0:
            return True
        if len(A) == 0:
            return False
        
        # 首先记录A中所有的字符以及它们的个数，然后遍历B，若
        # 出现小于0的情况，说明B中该字符出现的次数大于在A中出现的次数
        numTable = [0 for i in range(26)]
        for i in A:
            numTable[ord(i) - 65] += 1
        for i in B:
            if numTable[ord(i) - 65] == 0:
                return False
            else:
                numTable[ord(i) - 65] -= 1
        
        return True

# 主函数
if __name__ == "__main__":
    solution = Solution()
    A = "ABCD"
    B = "ACD"
    print("Input: A = ", A, ", B = ", B)
    print("Output: ", solution.compareStrings(A,B))



# 运行结果
# Input: A =  ABCD , B =  ACD
# Output:  True