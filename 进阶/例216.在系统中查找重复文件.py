# 问题描述
# 给定一个目录信息列表（包含目录路径），以及该目录中包含的所有文件，根据路径查找文件系统中所有重复文件组。
# 一组重复文件包含至少两个具有相同内容的文件。输入信息列表中的单个目录信息字符串格式如下：root/d1/d2/...
# /dm f1.txt(f1_content) f2.txt(f2_content) ... fn.txt(fn_content)，这代表目录root/d1/d2/.../dm
# 中有n个文件(f1.txt, f2.txt, ... , fn.txt， 内容分别为f1_content, f2_content, ... , fn_content)
# 注意n >= 1且m >= 0.若m = 0, 表示该目录是根目录
# 输出一个包含重复文件路径的列表，每组包含所有内容相同的文件路径。一个文件路径是具有以下格式的字符串
# directory_path/file_name.txt


# 示例
# 输入：["root/a 1.txt(abcd) 2.txt(efgh)", "root/c 3.txt(abcd)", "root/c/d 4.txt(efgh)",
# "root 4.txt(efgh)"]
# 输出：[["root/a/2.txt", "root/c/d/4.txt", "root/4.txt"], ["root/a/1.txt", "root/c/3.txt"]]


# 源码实现
import collections
class Solution:
    def findDuplicate(self, paths):
        dic = collections.defaultdict(list)
        for path in paths:
            root, *f = path.split(" ")
            for file in f:
                txt, content = file.split("(")
                dic[content] += root + "/" + txt,
        return [dic[key] for key in dic if len(dic[key]) > 1]

if __name__ == '__main__':
    paths = ["root/a 1.txt(abcd) 2.txt(efgh)","root/c 3.txt(abcd)","root/c/d 4.txt(efgh)"]
    s = Solution()
    print("输入：", paths)
    print("输出：", s.findDuplicate(paths))


# 运行结果
# 输入： ['root/a 1.txt(abcd) 2.txt(efgh)', 'root/c 3.txt(abcd)', 'root/c/d 4.txt(efgh)']
# 输出： [['root/a/1.txt', 'root/c/3.txt'], ['root/a/2.txt', 'root/c/d/4.txt']]