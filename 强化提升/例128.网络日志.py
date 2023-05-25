# 问题描述
# 网络日志的记录，实现下面两个过程：hit(timestamp)建立一时间戳，get_hit_count_in_last_5_minutes(timestamp)
# 得到最后5分钟时间戳的个数


# 示例
# 输入：
# hit(1)
# hit(2)
# get_hit_count_in_last_5_minutes(3)
# hit(300)
# get_hit_count_in_last_5_minutes(300)
# get_hit_count_in_last_5_minutes(301)
# 输出：
# 2
# 3
# 2

# 输入：
# hit(1)
# hit(1)
# hit(1)
# hit(2)
# get_hit_count_in_last_5_minutes(3)
# hit(300)
# get_hit_count_in_last_5_minutes(300)
# get_hit_count_in_last_5_minutes(301)
# get_hit_count_in_last_5_minutes(302)
# get_hit_count_in_last_5_minutes(900)
# 输出：
# 4
# 5
# 2
# 1
# 0
# 0


# 源码实现
class WebLogger:
    def __init__(self):
        self.Q = []
    
    def hit(self, timestamp):
        self.Q.append(timestamp)
    
    def get_hit_count_in_last_5_minutes(self, timestamp):
        if self.Q == []:
            return 0
        i = 0
        n = len(self.Q)
        while i < n and self.Q[i] + 300 <= timestamp:
            i += 1
        self.Q = self.Q[i:]
        return len(self.Q)

# 主函数
if __name__ == '__main__':
    s = WebLogger()
    print("Input: hit(1),hit(2)")
    s.hit(1)
    s.hit(2)
    print("Output: ")
    print(s.get_hit_count_in_last_5_minutes(3))
    print("Input: hit(300)")
    s.hit(300)
    print("Output: ")
    print(s.get_hit_count_in_last_5_minutes(300))
    print("Output: ")
    print(s.get_hit_count_in_last_5_minutes(301))


# 运行结果
# Input: hit(1),hit(2)
# Output:
# 2
# Input: hit(300)
# Output:
# 3
# Output:
# 2