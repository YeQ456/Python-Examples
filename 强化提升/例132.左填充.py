# 问题描述
# 实现一个leftpad方法，在字符串的左侧添加符号。符号可以是空格，也可以是规定的符号


# 示例
# 输入：leftpad("foo",5)
# 输出："##foo"
# 解释：要求字符串总长度为5，不足之处用空格在左填充

# 输入：leftpad("foobar",6)
# 输出："foobar"
# 解释：要求字符串总长度为6

# 输入：leftpad("1",2,"0")
# 输出：01
# 解释：要求字符串总长度为2，不足之处用字符0填充


# 源码实现
class StringUtils:
    def leftpad(self, originalStr, size, padChar = ' '):
        return padChar * (size - len(originalStr)) + originalStr

# 主函数
if __name__ == '__main__':
    size = 8
    str1 = "foobar"
    s = StringUtils()
    print("Input: ", str1)
    print("Output: ", s.leftpad(str1,size))


# 运行结果
# Input:  foobar
# Output:    foobar