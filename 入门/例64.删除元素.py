# 问题描述
# 给定一个数组合一个值，在原地删除与值相同的数字，返回新数组的长度。元素的顺序可以改变，对新的数组
# 不会有影响


# 示例
# 输入：[0,4,4,0,0,2,4,4], value = 4
# 输出：4
# 解释：删除后的数组为[0,0,0,2]，有4个元素，长度为4


# 源码实现
class Solution:
    def removeElement(self, A, elem):
        j = len(A) - 1
        for i in range(len(A) - 1, -1, -1):
            if A[i] == elem:
                A[i], A[j] = A[j], A[i]
                j -= 1
        
        return j + 1

# 主函数
if __name__ == '__main__':
    solution = Solution()
    A = [0,4,4,0,0,2,4,4]
    elem = 4
    ans = solution.removeElement(A,elem)
    print("Input: A = ", A, ", value = ", elem)
    print("Output: ", ans)



# 运行结果
# Input: A =  [0, 0, 2, 0, 4, 4, 4, 4] , value =  4
# Output:  4