# 问题描述
# 有n个人，编号分别为1,2,...,n，n为偶数。选择其中的一半人，有C(n, n/2)种组合方式，每一种组合方式按照
# 编号从小到大排序，再将已排序的组合方式按照字典序排序，求第k种组合方式
# 字典序定义：首先比较两个字符串长度，长度小的字典序小，若长度相同，则从字符串左边开始逐位比较，
# 找到第一位不同的字符，对应字符小的字符串，字典序小


# 示例
# 输入：n = 2, k = 1
# 输出：[1]
# 解释：组合方式按照字典序排序：[1],[2]

# 输入：n = 4, k = 2
# 输出：[3]
# 解释：组合方式按照字典序排序：[1,2], [1,3], [1,4], [2,3], [2,4], [3,4]


# 源码实现
class Solution:
    def getCombination(self, n, k):
        C = [[0] * (n + 1) for i in range(n + 1)]
        for i in range(n + 1):
            C[i][0] = 1
            C[i][i] = 1
        
        for i in range(1, n + 1):
            for j in range(1, i):
                C[i][j] = C[i - 1][j - 1] + C[i - 1][j]
        
        ans = []
        curr_index = 1
        for i in range(1, n // 2 + 1):
            base = C[n - curr_index][n // 2 - i]
            while k > base:
                curr_index = curr_index + 1
                base = base + C[n - curr_index][n // 2 - i]
            
            base = base - C[n - curr_index][n // 2 - i]
            k = k - base
            ans.append(curr_index)
            curr_index = curr_index + 1
        
        return ans

# 主函数
if __name__ == '__main__':
    n = 4
    k = 2
    solution = Solution()
    print("Input: n = ", n, ", k = ", k)
    print("Output: ", solution.getCombination(n, k))



# 运行结果
# Input: n =  4 , k =  2
# Output:  [1, 3]