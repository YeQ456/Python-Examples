# 问题描述
# 给定一系列描述函数进入和退出的时间，问：每个函数的运行时间为多少


# 示例
# 输入：s = ["F1 Enter 10", "F2 Enter 18", "F2 Exit 19", "F1 Exit 20"]
# 输出：["F1|10", "F2|1"]
# 解释：F1从10时刻进入，20时刻退出，运行时长为10,；F2从18时刻进入，19时刻退出，运行时长为1

# 输入：s = ["F1 Enter 10", "F1 Exit 18", "F1 Enter 19", "F1 Exit 20"]
# 输出：["F1|9"]
# 解释：F1从10时刻进入，18时刻退出；又从19时刻进入，20时刻退出，总运行时长为9


# 源码实现
class Solution:
    def getRuntime(self, s):
        map = {}
        for i in s:
            count = 0
            while not i[count] == ' ':
                count = count + 1
            fun = i[0:count]
            if i[count + 2] == 'n':
                count = count + 7
                v = int(i[count:len(i)])
                if fun in map.keys():
                    map[fun] = v - map[fun]
                else:
                    map[fun] = v
            else:
                count = count + 6
                v = int(i[count:len(i)])
                map[fun] = v - map[fun]
        
        res = []
        for i in map:
            res.append(i)
        
        res.sort()
        for i in range(0,len(res)):
            res[i] = res[i] + '|' + str(map[res[i]])
        
        return res

# 主函数
if __name__ == '__main__':
    s = ["F1 Enter 10", "F2 Enter 18", "F2 Exit 19", "F1 Exit 20"]
    solution = Solution()
    print("Input: s = ", s)
    print("Output: ", solution.getRuntime(s))



# 运行结果
# Input: s =  ['F1 Enter 10', 'F2 Enter 18', 'F2 Exit 19', 'F1 Exit 20']
# Output:  ['F1|10', 'F2|1']