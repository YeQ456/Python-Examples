# 问题描述
# 给定化学式(以字符串形式给出)，返回每种元素原子的数量。原子始终以大写字符开头，以零或多个小写字母
# 表示名称


# 示例
# 输入：化学式为H2O
# 输出：H2O
# 解释：原子个数分别为：H2个，O1个


# 源码实现
import re
import collections
class Solution(object):
    def countOfAtoms(self, formula):
        parse = re.findall(r"([A-Z][a-z]*)(\d*)|(\()|(\))(\d*)", formula)
        stack = [collections.Counter()]
        for name, m1, left_open, right_open, m2 in parse:
            if name:
                stack[-1][name] += int(m1 or 1)
            if left_open:
                stack.append(collections.Counter())
            if right_open:
                top = stack.pop()
                for k in top:
                    stack[-1][k] += top[k] * int(m2 or 1)
        
        return "".join(name + (str(stack[-1][name]) if stack[-1][name] > 1 else '') for name in sorted(stack[-1]))
    
# 主函数
if __name__ == '__main__':
    solution = Solution()
    Test_in = "H2O"
    Test_out = solution.countOfAtoms(Test_in)
    print("Input: ", Test_in)
    print("Output: ", Test_out)



# 运行结果
# Input:  H2O
# Output:  H2O