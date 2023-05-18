# 问题描述
# 输入一个英文句子，将每个单词的首字母改成大写


# 示例
# 输入：s = "i want to go home"
# 输出："I Want To Go Home"

# 输入：s = "we want to go to school"
# 输出："We Want To Go To School"


# 源码实现
class Solution:
    def capitalizesFirst(self, s):
        n = len(s)
        s1 = list(s)
        if s1[0] >= 'a' and s1[0] <= 'z':
            s1[0] = chr(ord(s1[0]) - 32)
        for i in range(1, n):
            if s1[i - 1] == ' ' and s1[i] != ' ':
                s1[i] = chr(ord(s1[i]) - 32)
        
        return ''.join(s1)

# 主函数
if __name__ == '__main__':
    s = "i am from bupt"
    solution = Solution()
    print("Input: s = ", s)
    print("Output: ", solution.capitalizesFirst(s))



# 运行结果
# Input: s =  i am from bupt
# Output:  I Am From Bupt