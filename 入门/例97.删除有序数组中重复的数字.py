# 问题描述
# 给定一个有序数组，删除其中的重复元素，使得每个数字最多出现2次，返回新的数组的长度。若一个数字出现
# 超过2次，则保留最后2个


# 示例
# 输入：[1,1,1,2,2,3]
# 输出：5
# 解释：新数组长度为5，新数组为[1,1,2,2,3]


# 源码实现
class Solution:
    def removeDuplicates(self, A):
        B = []
        before = None
        countb = 0
        for number in A:
            if(before != number):
                B.append(number)
                before = number
                countb = 1
            elif countb < 2:
                B.append(number)
                countb += 1
        p = 0
        for number in B:
            A[p] = number
            p += 1
        return p

# 主函数
if __name__ == '__main__':
    s = Solution()
    A = [1,1,1,2,2,3]
    p = s.removeDuplicates(A)
    print("Input: ", A)
    print("Output: ", p)



# 运行结果
# Input:  [1, 1, 2, 2, 3, 3]
# Output:  5