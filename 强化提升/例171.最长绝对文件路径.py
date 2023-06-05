# 问题描述
# 通过以下方式用字符串抽象文件系统：字符串"dir\n\tsubdirl\n\tsubdir2\n\t\tfile.ext"代表目录dir
# 包含一个空子目录subdir1和一个包含文件file.ext的子目录subdir2
#
# 字符串"dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\
# tfile2.ext"代表如下文件结构：
#  dir
#    subdir1
#        file1.ext
#        subsubdir1
#    subdir2
#        subsubdir2
#           file2.ext
#
# 给定一个以上述格式表示文件系统的字符串，返回抽象文件系统中文件最长绝对路径的长度。若系统中没有
# 文件，则返回0.规则：一个文件名至少包含一个"."和扩展名;目录或子目录的名称不包含"."


# 示例
# 输入："dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext"
# 输出：20

# 输入："dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\b\t\tsubsubdir2\n\t\t\
# tfile2.ext"
# 输出：32
# 解释：字符串“dir/subdir2/subsubdir2/file2.ext"的字符串长度为32


# 源码实现
import re
import collections
class Solution:
    def lengthLongestPath(self, input):
        dict = collections.defaultdict(lambda: "")
        lines = input.split("\n")
        n = len(lines)
        result = 0
        for i in range(n):
            count = lines[i].count("\t")
            lines[i] = dict[count - 1] + re.sub("\\t+", "/", lines[i])
            if "." in lines[i]:
                result = max(result, len(lines[i]))
            dict[count] = lines[i]
        return result

# 主函数
if __name__ == '__main__':
    words = "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"
    s = Solution()
    print("Input: ", words)
    print("Output: ", s.lengthLongestPath(words))


# 运行结果
# Input:  dir
#         subdir1
#                 file1.ext
#                 subsubdir1
#         subdir2
#                 subsubdir2
#                         file2.ext
# Output:  32