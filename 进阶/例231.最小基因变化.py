# 问题描述
# 基因序列可以用8个字符串表示，可以选择的字符包括A、C、G、T。假设需要从起点到结束点调查基因突变（基因
# 序列中的单个字符发生突变，如"AACCCGGTT" -> "AACCGGTA"是1个突变）。此外，还有一个给定的基因库，记
# 录了所有有效的基因突变，基因突变必须在基因库中才有效
# 给出3个参数起始点、结束点、基因库，确定从起始点到结束点变异所需的最小突变数；若没有这样的突变，则
# 返回-1


# 示例
# 输入起始点："AACCGGTT"，结束点："AACCGGTA"，基因库为["AACCGGTA"]
# 输出：1
# 结束：只需发生一次突变，且突变在基因库中


# 源码实现
from collections import deque
class Solution:
    def minMutation(self, start, end, bank):
        if not bank:
            return -1
        bank = set(bank)
        h = deque()
        h.append((start, 0))
        while h:
            seq, step = h.popleft()
            if seq == end:
                return step
            for c in "ACGT":
                for i in range(len(seq)):
                    new_seq = seq[:i] + c + seq[i + 1:]
                    if new_seq in bank:
                        h.append((new_seq, step + 1))
                        bank.remove(new_seq)
        return -1

if __name__ == '__main__':
    s = Solution()
    n = "AACCGGTT"
    m = "AACCGGTA"
    p = ["AACCGGTA"]
    print("输入起始点：", n)
    print("输入结束点：", m)
    print("输入基因库：", p)
    print("输出步数：", s.minMutation(n,m,p))


# 运行结果
# 输入起始点： AACCGGTT    
# 输入结束点： AACCGGTA    
# 输入基因库： ['AACCGGTA']
# 输出步数： 1