# 问题描述
# 为网站设计一个负载均衡器，提供如下3个功能：添加1台新的服务器到整个集群中add(server_id)。从集群中
# 删除1个服务器remove(server_id)。在集群中随机（等概率）选择1个有效的服务器pick()。最开始时，集群中
# 没有服务器，每次pick()调用时，需要在集群中随机返回1个server_id


# 示例
# 输入：
# add(1)
# add(2)
# add(3)
# pick()
# pick()
# pick()
# pick()
# remove(1)
# pick()
# pick()
# pick()
# 输出：
# 1
# 2
# 1
# 3
# 2
# 3
# 3

# 输入：
# add(1)
# add(2)
# remove(1)
# pick()
# pick()
# 输出：
# 2
# 2


# 源码实现
class LoadBalancer:
    def __init__(self):
        self.server_ids = []
        self.id2index = {}
    
    def add(self, server_id):
        if server_id in self.id2index:
            return
        self.server_ids.append(server_id)
        self.id2index[server_id] = len(self.server_ids) - 1
    
    def remove(self, server_id):
        if server_id not in self.id2index:
            return
        index = self.id2index[server_id]
        del self.id2index[server_id]
        last_server_id = self.server_ids[-1]
        self.id2index[last_server_id] = index
        self.server_ids[index] = last_server_id
        self.server_ids.pop()
    
    def pick(self):
        import random
        index = random.randint(0, len(self.server_ids) - 1)
        return self.server_ids[index]

# 主函数
if __name__ == '__main__':
    s = LoadBalancer()
    s.add(1)
    s.add(2)
    s.remove(1)
    print("Input: \nadd(1)\nadd(2)\nremove(1)")
    print("Output: ", s.pick())
    print("Output: ", s.pick())


# 运行结果
# Input: 
# add(1)
# add(2)
# remove(1)
# Output:  2
# Output:  2