# 问题描述
# 给一个非负整数n，根据数字以英文单词输出数字大小


# 示例
# 输入：10245
# 输出："ten thousand two hundred forty five"


# 源码实现
class Solution:
    def covertWords(self, number):
        n1 = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten",
              "eleven", "twelve", "thirteen", "fourteen", "nineteen"
            ]
        
        n2 = ["", "ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty",
              "ninety"  
            ]
        
        n3 = ['hundred', '', 'thousand', 'million', 'billion']

        res = ''
        index = 1
        if number == 0:
            return 'zero'
        elif 0 < number < 20:
            return n1[number]
        elif 20 <= number < 100:
            return n2[number // 10] + ' ' + n1[number]
        else:
            while number != '':
                digit = int(str(number)[-3::])
                number = (str(number)[:-3:])
                i = len(str(digit))
                r = ''
                while True:
                    if digit < 20:
                        r += n1[digit]
                        break
                    elif 20 <= digit < 100:
                        r += n2[digit // 10] + ' '
                    elif 100 <= digit < 1000:
                        r += n1[digit // 100] + ' ' + n3[0] + ' '
                    digit = digit % (10 ** (i - 1))
                    i -= 1
                if digit != 0:
                    r += ' ' + n3[index] + ' '
                index += 1
                r += res
                res = r
        return res.strip()

# 主函数
if __name__ == '__main__':
    s = Solution()
    n = 10245
    print("Input: ", n)
    print("Output: ", s.covertWords(n))


# 运行结果
# Input:  10245
# Output:  ten thousand two hundred forty five