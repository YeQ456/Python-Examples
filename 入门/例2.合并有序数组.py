# 问题描述
# 合并两个升序的整数数组A和B，合并后的数组也要保证有序

# 示例
# 输入：A = [1], B = [1]
# 输出：[1,1]

# 输入：A = [1,2,3,4], B = [2,4,5,6]
# 输出：[1,2,2,3,4,4,5,6]

# 源码实现
class Solution:
    def mergeSortedArray(self, A, B):
        i, j = 0, 0
        res = []
        while i < len(A) and j < len(B):
            if A[i] < B[j]:
                res.append(A[i])
                i += 1
            else:
                res.append(B[j])
                j += 1
        
        while i < len(A):
            res.append(A[i])
            i += 1
        
        while j < len(B):
            res.append(B[j])
            j += 1
        
        return res

# 主函数    
if __name__ == '__main__':
    A1 = [1,4]
    B1 = [1,2,3]
    A2 = [1,2,3,4]
    B2 = [2,3,4,5,6]
    solution = Solution()
    print("Input: ", A1, B1)
    print("Output: ", solution.mergeSortedArray(A1,B1))
    print("Input: ", A2, B2)
    print("Output: ", solution.mergeSortedArray(A2,B2))
   
  
# 运行结果
# Input:  [1, 4] [1, 2, 3]
# Output:  [1, 1, 2, 3, 4]
# Input:  [1, 2, 3, 4] [2, 3, 4, 5, 6]
# Output:  [1, 2, 2, 3, 3, 4, 4, 5, 6]
