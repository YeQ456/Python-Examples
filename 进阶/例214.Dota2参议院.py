# 问题描述
# 在DOTA2的世界中有两个党派：Radiant和Dire。DOTA2参议院的由来来自两党的参议员组成。现在参议院想要
# 对DOTA2游戏的变化作出决定，对此变化的投票是基于回合的。在每一回合中，每位参议员都可以行使以下两
# 项权利之一：1.禁止一位参议员的权利，即一个参议员可以让另一位参议员在这次以及随后的所有回合中失去
# 投票权；2.宣布胜利，即这位参议员如果发现仍然有投票权的参议员都来自同一方，他可以宣布胜利并作出关于
# 比赛变化的决定。
# 给出代表每个参议员所属党派的字符串。字符R和D分别代表Radiant方和Dire方。若有n个参议员，则给定字符串
# 的大小将为n
# 基于回合的过程从给定顺序的第一个参议员开始。程序将持续到投票结束。在此过程中，所有失去投票权的参议员
# 都将被跳过。
# 假设每个参议员足够聪明且将为自己的政党发挥最佳策略。预测哪一方最终宣布胜利并使DOTA2比赛进行政变，输出
# 应为Radiant或Dire


# 示例
# 输入：RD
# 输出：Radiant
# 解释：第1位参议员来自Radiant，他可以禁止下一位参议员在第1轮的权利。第2位参议员不能再行使任何权利，
# 因为他的权利已经被禁止。在第2轮选举中，第1位参议员可以宣布胜利，因为他是参议院中唯一可以投票的人

# 输入：RDD
# 输出：Dire


# 源码实现
from collections import deque
class Solution:
    def predictPartyVictory(self, senate):
        senate = deque(senate)
        while True:
            try:
                thisGuy = senate.popleft()
                if thisGuy == 'R':
                    senate.remove('D')
                else:
                    senate.remove('R')
                senate.append(thisGuy)
            except:
                return 'Radiant' if thisGuy == 'R' else 'Dire'

if __name__ == '__main__':
    s = Solution()
    senate = "RD"
    print("输入：", senate)
    print("输出：", s.predictPartyVictory(senate))


# 运行结果
# 输入： RD     
# 输出： Radiant