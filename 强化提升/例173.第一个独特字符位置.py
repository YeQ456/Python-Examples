# 问题描述
# 给出一个字符串，找到字符串中第一个不重复的字符，返回它的下标。若不存在则返回-1


# 示例
# 输入：s = "longterm"
# 输出：0

# 输入：s = "lovelongterm"
# 输出：2


# 源码实现
class Solution:
    def firstUniqChar(self, s):
        alp = {}
        for c in s:
            if c not in alp:
                alp[c] = 1
            else:
                alp[c] += 1
        index = 0
        for c in s:
            if alp[c] == 1:
                return index
            index += 1
        return -1

# 主函数
if __name__ == '__main__':
    s = "lintcode"
    ss = Solution()
    print("Input: ", s)
    print("Output: ", ss.firstUniqChar(s))


# 运行结果
# Input:  lintcode
# Output:  0