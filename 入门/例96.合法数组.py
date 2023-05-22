# 问题描述
# 若数组中只包含1个出现了奇数次的数，则数组合法，否则数组不合法。输入一个只包含正整数的数组a，判断该
# 数组是否合法，若合法返回出现奇数次的数，否则返回-1


# 示例
# 输入：a = [1,1,2,2,3,4,4,5,5]
# 输出：3
# 解释：该数组只有3出现了奇数次，数组合法，返回3

# 输出：a = [1,1,2,2,3,4,4,5]
# 输出：-1
# 解释：该数组中3和5都出现了奇数次，因此数组不合法，返回-1


# 源码实现
class Solution:
    def isValid(self, a):
        countSet = {}
        for i in a:
            if i in countSet:
                countSet[i] += 1
            else:
                countSet[i] = 1
        isHas = False
        for key in countSet:
            if countSet[key] % 2 == 1:
                if isHas:
                    return -1
                else:
                    isHas = True
                    ans = key
        if isHas:
            return ans
        return -1

# 主函数
if __name__ == '__main__':
    a = [1,1,2,2,3,3,4,4,5,5]
    s = Solution()
    print("Input: ", a)
    print("Output: ", s.isValid(a))



# 运行结果
# Input:  [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]
# Output:  -1