# 问题描述
# 给定一个字符串S，可以将其中所有的字符任意切换大小写，得到一个新的字符串。将所有可生成的新字符串以一个
# 列表的形式输出


# 示例
# 输入：S = a1b2
# 输出：["a1b2","a1B2","A1b2","A1B2"]


# 源码实现
class Solution(object):
    def letterCasePermutations(self, S):
        res = []
        indices = []
        indices = [i for i, j in enumerate(S) if S[i].isalpha()]
        for i in range(0, pow(2, len(indices))):
            if i == 0:
                res.append(S)
            else:
                j = i
                bpos = 0
                nsl = list(S)
                while j > 0:
                    ci2c = indices[bpos]
                    if j & 1 and S[ci2c].islower():
                        nsl[ci2c] = S[ci2c].upper()
                    elif j & 1 and S[ci2c].isupper():
                        nsl[ci2c] = S[ci2c].lower()
                    bpos += 1
                    j = j >> 1
                res.append("".join(nsl))
        
        return res

# 主函数
if __name__ == '__main__':
    solution = Solution()
    S = "a1b2"
    print("Input: S = ", S)
    print("Output: ", solution.letterCasePermutations(S))



# 运行结果
# Input: S =  a1b2
# Output:  ['a1b2', 'A1b2', 'a1B2', 'A1B2']