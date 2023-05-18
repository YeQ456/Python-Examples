# 问题描述
# 给出一个由字母A和B组成的字符串S，找出一个最长的子串，要求这个子串里面A和B的数量相同，输出该子串长度


# 示例
# 输入：S = "ABAAABBBA"
# 输出：8
# 解释：子串S[0,7]和子串S[1,8]满足条件，长度为8

# 输入：S = "AAAAAA"
# 输出：0
# 解释：字符串S中除了空字符串，不存在A和B数量相同的子串


# 源码实现
class Solution:
    def getsubString(self, S):
        ans = 0
        arr = [0 for i in range(len(S))]
        sets = {}
        if S[0] == 'A':
            arr[0] = 1
            sets[1] = 0
        else:
            arr[0] = -1
            sets[-1] = 0
        for i in range(1,len(S)):
            if S[i] == 'A':
                arr[i] = arr[i - 1] + 1
                if arr[i] == 0:
                    ans = i + 1
                    continue
                if arr[i] in sets:
                    ans = max(ans, i - sets[arr[i]])
                else:
                    sets[arr[i]] = i
            else:
                arr[i] = arr[i - 1] - 1
                if arr[i] == 0:
                    ans = i + 1
                    continue
                if arr[i] in sets:
                    ans = max(ans, i - sets[arr[i]])
                else:
                    sets[arr[i]] = i
        
        return ans

# 主函数
if __name__ == '__main__':
    S = "ABABAB"
    solution = Solution()
    print("Input: S = ", S)
    print("Output: ", solution.getsubString(S))



# 运行结果
# Input: S =  ABABAB
# Output:  6