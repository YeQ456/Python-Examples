# 问题描述
# 给一个词典，找出其中最长的单词


# 示例
# 输入：{"dog","google","facebook","internationalization","blabla"}
# 输出：["internationalization"]

# 输入：{"like","love","hate","yes"}
# 输出：["like","love","hate"]


# 源码实现
class Solution:
    def longestWords(self, dictionary):
        answer = []
        maxLength = 0
        for item in dictionary:
            if len(item) > maxLength:
                maxLength = len(item)
                answer = [item]
            elif len(item) == maxLength:
                answer.append(item)
        
        return answer

# 主函数
if __name__ == '__main__':
    solution = Solution()
    dic = ["dog","google","facebook","internationalization","blabla"]
    answer = solution.longestWords(dic)
    print("Input: ", dic)
    print("Output: ", answer)



# 运行结果
# Input:  ['dog', 'google', 'facebook', 'internationalization', 'blabla']
# Output:  ['internationalization']