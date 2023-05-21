# 问题描述
# 报数序列是指一个整数序列，按照顺序报数，根据报数得到下一个数。规模如下：第一个数为1，读作“一个一”，
# 即11，也即是第二个数是11；11读作“两个一”，即21，也即是第三个数是21.21读作“一个二，一个一”，即
# 1211，也即是第四个数为1211.现在给定一个正整数n，输出报数序列的第n项。注：整数顺序将表示为一个
# 字符串


# 示例
# 输入：5
# 输出：111221


# 源码实现
class Solution:
    def countAndSay(self, n):
        string = '1'
        for i in range(n - 1):
            a = string[0]
            count = 0
            s = ''
            for ch in string:
                if a == ch:
                    count += 1
                else:
                    s += str(count) + a
                    a = ch
                    count = 1
            s += str(count) + a
            string = s
            a = string[0]
        
        return string

# 主函数
if __name__ == '__main__':
    num = 5
    solution = Solution()
    print("Input: ", num)
    print("Output: ", solution.countAndSay(num))



# 运行结果
# Input:  5
# Output:  111221