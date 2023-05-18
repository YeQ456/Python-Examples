# 问题描述
# 给定两个字符串S和T，判断S能否通过删除一些字母(包含0个)变成T


# 示例
# 输入：S = "longterm", T = "long"
# 输出：True


# 源码实现
class Solution:
    def canConvert(self, s, t):
        j = 0
        for i in range(len(s)):
            if s[i] == t[j]:
                j += 1
                if j == len(t):
                    return True
        
        return False

# 主函数
if __name__ == '__main__':
    s = "longterm"
    t = "long"
    solution = Solution()
    print("Input: s = ", s, ", t = ", t)
    print("Output: ", solution.canConvert(s,t))



# 运行结果
# Input: s =  longterm , t =  long
# Output:  True