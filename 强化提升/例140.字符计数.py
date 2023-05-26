# 问题描述
# 对字符串中的字符进行计数，返回hashmap。key为字符，value是这个字符出现的次数


# 示例
# 输入：str = "abca"
# 输出：{"a": 2, "b" : 1, "c" : 1}

# 输入：str = "ab"
# 输出：{"a" : 1, "b" : 1}


# 源码实现
class Solution:
    def countCharacters(self, str):
        map = dict()
        for c in str:
            map[c] = map.get(c, 0) + 1
        return map

# 主函数
if __name__ == '__main__':
    str1 = "abca"
    s = Solution()
    print("Input: ", str1)
    print("Output: ", s.countCharacters(str1))


# 运行结果
# Input:  abca
# Output:  {'a': 2, 'b': 1, 'c': 1}