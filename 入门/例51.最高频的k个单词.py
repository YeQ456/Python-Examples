# 问题描述
# 给一个单词列表，求出这个列表中出现频次最高的k个单词


# 示例
# 输入：
#       [
#          "yes", "long", "code",
#          "yes", "code", "baby",
#          "you", "baby", "chrome",
#          "safari", "long", "code",
#          "body", "long", "code"
#       ]
#       k = 3
# 输出：["code","long","baby"]

# 输入：
#       [
#          "yes", "long", "code",
#          "yes", "code", "baby",
#          "you", "baby", "chrome",
#          "safari", "long", "code",
#          "body", "long", "code"
#       ]
#       k = 4
# 输出：["code","long","baby","yes"]


# 源码实现
class Solution:
    def topKFrequentWords(self, words, k):
        dict = {}
        res = []
        for word in words:
            if word not in dict:
                dict[word] = 1
            else:
                dict[word] += 1
        
        sorted_d = sorted(dict.items(), key=lambda x:x[1], reverse=True)
        for i in range(k):
            res.append(sorted_d[i][0])
        
        return res

# 主函数
if __name__ == '__main__':
    nums = [
             "yes", "long", "code",
             "yes", "code", "baby",
             "you", "baby", "chrome",
             "safari", "long", "code",
             "body", "long", "code"
            ]
    k = 4
    solution = Solution()
    print("Input: ", nums)
    print("Input: k = ", k)
    print("Output: ", solution.topKFrequentWords(nums, k))



# 运行结果
# Input:  ['yes', 'long', 'code', 'yes', 'code', 'baby', 'you', 'baby', 'chrome', 'safari', 'long', 'code', 'body', 'long', 'code']
# Input: k =  4
# Output:  ['code', 'long', 'yes', 'baby']