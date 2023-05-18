# 问题描述
# 把字符串S中的字符从左到右写入行中，每行最大宽度为100，若往后新写一个字符导致该行宽度超过100，则写入
# 下一行。
# 其中，一个字符的宽度由一个给定数组widths决定，widths[0]是字符a的宽度，widths[1]是字符b的宽度,...,
# widths[25]是字符z的宽度
# 把字符串S全部写完，至少需要多少行？最后一行用去的宽度是多少？返回一个整数列表


# 示例
# 输入：widths = [10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10]
#      S = "abcdefghijklmnopqrstuvwxyz"
# 输出：[3, 60]
# 解释：每个字符的宽度都为10，为了把这26个字符都写进去，需要两个整行和一个长度为60的行


# 源码实现
class Solution:
    def numberOfLines(self, widths, S):
        line = 1
        space = 0
        flag = False
        for c in S:
            if flag:
                line += 1
                flag = False
            space += widths[ord(c) - 97]
            if space > 100:
                line += 1
                space = widths[ord(c) - 97]
            elif space == 100:
                space = 0
                flag = True
        
        return [line,space]

# 主函数
if __name__ == '__main__':
    solution = Solution()
    widths = [10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10]
    S = "abcdefghijklmnopqrstuvwxyz"
    print("Input: width = ", widths)
    print("Input: S =", S)
    print("Output: ", solution.numberOfLines(widths, S))



# 运行结果
# Input: width =  [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
# Input: S = abcdefghijklmnopqrstuvwxyz
# Output:  [3, 60]