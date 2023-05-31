# 问题描述
# 给出一个字符串s及n个子字符串。可以从字符串s中循环移除n个子串中的任意一个，使得剩下字符串s的长度最小，
# 输出这个最小长度


# 示例
# 输入："ccdaabcdbb", 子串：["ab", "cd"]
# 输出：2

# 输入："abcabd", 子串：["ab", "abcd"]
# 输出：0


# 源码实现
class Solution:
    def minLength(self, s, dict):
        import queue
        que = queue.Queue()
        que.put(s)
        hash = set([s])
        min = len(s)
        while not que.empty():
            s = que.get()
            for sub in dict:
                found = s.find(sub)
                while found != -1:
                    new_s = s[:found] + s[found + len(sub):]
                    if new_s not in hash:
                        if len(new_s) < min:
                            min = len(new_s)
                        que.put(new_s)
                        hash.add(new_s)
                    found = s.find(sub, found + 1)
        return min

# 主函数
if __name__ == '__main__':
    str1 = "ccdaabcdbb"
    k = ["ab","cd"]
    s = Solution()
    print("Input: ", str1, ", k = ",k)
    print("Output: ", s.minLength(str1, k))


# 运行结果
# Input:  ccdaabcdbb , k =  ['ab', 'cd']
# Output:  2