# 问题描述
# 写一个方法，输入给定字符串，翻转字符串中的元音字母


# 示例
# 输入：s = "hello"
# 输出："holle"


# 源码实现
class Solution:
    def reverseVowels(self, s):
        vowels = set(["a","e","i","o","u","A","E","I","O","U"])
        res = list(s)
        start, end = 0, len(res) - 1
        while start <= end:
            while start <= end and res[start] not in vowels:
                start += 1
            while start <= end and res[end] not in vowels:
                end -= 1
            if start <= end:
                res[start], res[end] = res[end], res[start]
                start += 1
                end -= 1
        return "".join(res)

# 主函数
if __name__ == '__main__':
    s = Solution()
    x = "hello"
    print("Input: s = ", x)
    print("Output: ", s.reverseVowels(x))



# 运行结果
# Input: s =  hello
# Output:  holle