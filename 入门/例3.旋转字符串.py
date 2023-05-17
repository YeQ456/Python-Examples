# 问题描述
# 给定一个字符串和一个偏移量，根据偏移量原地从左向右旋转字符串
# 注：尽量不使用新的空间，即O(1)


# 示例
# 输入：str = "abcdefg", offset = 3
# 输出："efgabcd"

# 输入：str = "abcdefg", offset = 0
# 输出："abcdefg"

# 输入：str = "abcdefg", offset = 1
# 输出："gabcdef"

# 输入：str = "abcdefg", offset = 2
# 输出："fgabcde"


# 源码实现
class Solution:
    def rotateString(self, str, offset):
        if len(str) > 0:
            offset = offset % len(str)
        
        temp = (str + str)[len(str) - offset : 2 * len(str) - offset]
        for i in range(len(temp)):
            str[i] = temp[i]

# 主函数    
if __name__ == '__main__':
    str = ["a","b","c","d","e","f","g"]
    offset = 3
    solution = Solution()
    solution.rotateString(str,offset)
    print("Input: str = ", ["a","b","c","d","e","f","g"], " ", "offset = ", offset)
    print("Output: ", str);
  
  
# 运行结果
# Input: str =  ['a', 'b', 'c', 'd', 'e', 'f', 'g']   offset =  3
# Output:  ['e', 'f', 'g', 'a', 'b', 'c', 'd']
