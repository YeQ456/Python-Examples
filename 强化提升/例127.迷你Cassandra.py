# 问题描述
# Cassandra是一个NoSQL数据库。Cassandra中的一个单独数据条目由row_key、colume_key、value3部分组成。
# row_key相当于哈希值，不支持范围查询，简化为字符串。colume_key已排序并支付范围查询，简化为整数。
# value是一个值，用于储存数据序列转化成的字符串。现在要实现insert(row_key,column_key,value)和
# query(row_key,column_start,column_end)，返回条目列表


# 示例
# 输入：
# insert("google",1,"abcd")
# query("google",0,1)
# 输出：[(1,"abcd")]

# 输入：
# insert("google",1,"abcd")
# insert("baidu",1,"efgh")
# insert("google",2,"hijk")
# query("google",0,1)
# query("google",0,2)
# query("go",0,1)
# query("baidu",0,10)
# 输出：
# [(1,"abcd")]
# [(1,"abcd"),(2,"hijk")]
# []
# [(1,"efgc")]


# 源码实现
class Column:
    def __init__(self, key, value):
        self.key = key
        self.value = value

from collections import OrderedDict
class Solution:
    def __init__(self):
        self.hash = {}
    
    def insert(self, row_key, column_key, column_value):
        if row_key not in self.hash:
            self.hash[row_key] = OrderedDict()
        self.hash[row_key][column_key] = column_value
    
    def query(self, row_key, column_start, column_end):
        rt = []
        if row_key not in self.hash:
            return rt
        self.hash[row_key] = OrderedDict(sorted(self.hash[row_key].items()))
        for key, value in self.hash[row_key].items():
            if key >= column_start and key <= column_end:
                rt.append(Column(key, value))
        return rt

# 主函数
if __name__ == '__main__':
    col1 = Column(1,"abcd")
    col2 = Column(2,"hijk")
    s = Solution()
    s.insert("google",col1.key, col1.value)
    s.insert("google",col2.key, col2.value)
    ls = s.query("google",0,2)
    print('Input: query("google",0,2)')
    print("Output: ")
    for i in ls:
        print(i.key, i.value)


# 运行结果
# Input: query("google",0,2)
# Output:
# 1 abcd
# 2 hijk