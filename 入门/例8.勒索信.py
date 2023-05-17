# 问题描述
# 给定一个表示勒索信内容的字符串和另一个表示杂志内容字符串，写一个方法来判断能否通过剪下杂志中的内容
# 构造出这封勒索信，若可以，返回True, 否则返回False。
# 注：杂志字符串中的每一个字符只能使用一次


# 示例
# 输入：ransomNote = "aa", magazine = "aab"
# 输出：True
# 解释：勒索信的内容可以从杂志内容剪辑而来


# 源码实现
class Solution:
    def LetterConstruct(self, ransomNote, magazine):
        arr = [0] * 26
        for c in magazine:
            arr[ord(c) - ord('a')] += 1
        for c in ransomNote:
            arr[ord(c) - ord('a')] -= 1
            if arr[ord(c) - ord('a')] < 0:
                return False
        
        return True

# 主函数
if __name__ == '__main__':
    solution = Solution()
    ransomNote = "aa"
    magazine = "aab"
    print("Input: 勒索信：", ransomNote, ", 杂志内容：", magazine)
    print("Output: ", solution.LetterConstruct(ransomNote, magazine))



# 运行结果
