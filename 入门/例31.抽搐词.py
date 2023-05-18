# 问题描述
# 正常单词不会有连续2个以上相同的字母，若出现连续3个以上的字母，那这是一个抽搐词。
# 给出该单词，从左到右求出所有抽搐字母的起点和终点


# 示例
# 输入：str = "whaaaaatttsup"
# 输出：[[2,6],[7,9]]
# 解释："aaa"和"ttt"是抽搐字母

# 输入：str = "whooooisssbesssst"
# 输出：[[2,5],[7,9],[12,15]]
# 解释："ooo" "sss" "ssss"都是抽搐字母


# 源码实现
class Solution:
    def twitchWords(self, str):
        n = len(str)
        c = str[0]
        left = 0
        ans = []
        for i in range(n):
            if str[i] != c:
                if i - left >= 3:
                    ans.append([left, i - 1])
                c = str[i]
                left = i
        
        if n - left >= 3:
            ans.append([left, n - 1])
        
        return ans

# 主函数
if __name__ == '__main__':
    str = "whooooisssbesssst"
    solution = Solution()
    print("Input: str = ", str)
    print("Output: ", solution.twitchWords(str))



# 运行结果
# Input: str =  whooooisssbesssst
# Output:  [[2, 5], [7, 9], [12, 15]]