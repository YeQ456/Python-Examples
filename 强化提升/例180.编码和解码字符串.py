# 问题描述
# 设计一个将字符串列表编码为字符串的算法。已经编码的字符串会通过网络发送，同时被解码到原始的字符串
# 列表，程序实现encode()和decode()


# 示例
# 输入：["long","term","love","you"]
# 输出：其中一种编码方式："long:;term;'love:;you"

# 输入：["we","say",":","yes"]
# 输出：其中一种编码方式："we:;say:;:::;yes"


# 源码实现
class Solution:
    def encode(self, strs):
        encoded = []
        for string in strs:
            for char in string:
                if char == ":":
                    encoded.append("::")
                else:
                    encoded.append(char)
            encoded.append(": ")
        return "".join(encoded)
    
    def decode(self, str):
        res = []
        idx = 0
        length = len(str)
        tmp_str = []
        while idx < length - 1:
            if str[idx] == ":":
                if str[idx + 1] == ":":
                    tmp_str.append(":")
                    idx += 2
                elif str[idx + 1] == " ":
                    res.append("".join(tmp_str))
                    tmp_str = []
                    idx += 2
            else:
                tmp_str.append(str[idx])
                idx += 1
        return res

# 主函数
if __name__ == '__main__':
    words = ["lint", "code", "love", "you"]
    s = Solution()
    print("Input: ", words)
    print("Encode: ", s.encode(words))
    print("Decode: ", s.decode(s.encode(words)))


# 运行结果
# Input:  ['lint', 'code', 'love', 'you']
# Encode:  lint: code: love: you:
# Decode:  ['lint', 'code', 'love', 'you']