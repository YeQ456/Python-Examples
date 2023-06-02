# 问题描述
# 给出一些Connections（Connections类），找出能够将所有城市都连接起来并花费最小的边。若可以将所有城市
# 都连接起来，返回这个连接方法；否则，返回一个空列表


# 示例
# 输入：Connections = ["Acity", "Bcity", 1], ["Acity", "Ccity", 2], ["Bcity", "Ccity", 3]
# 输出：["Acity", "Bcity", 1], ["Acity", "Ccity", 2]


# 源码实现
class Connection:
    def __init__(self, city1, city2, cost):
        self.city1, self.city2, self.cost = city1, city2, cost
    
    def comp(a, b):
        if a.cost != b.cost:
            return a.cost - b.cost
        if a.city1 != b.city1:
            if a.city1 < b.city1:
                return -1
            else:
                return 1
        if a.city2 == b.city2:
            return 0
        elif a.city2 < b.city2:
            return -1
        else:
            return 1

class Solution:
    def lowestCost(self, connections):
        cmp = 0
        hash = {}
        n = 0
        for connection in connections:
            if connection.city1 not in hash:
                n += 1
                hash[connection.city1] = n
            if connection.city2 not in hash:
                n += 1
                hash[connection.city2] = n
        father = [0 for i in range(n + 1)]
        results = []
        for connection in connections:
            num1 = hash[connection.city1]
            num2 = hash[connection.city2]
            root1 = self.find(num1, father)
            root2 = self.find(num2, father)
            if root1 != root2:
                father[root1] = root2
                results.append(connection)
        if len(results) != n - 1:
            return []
        return results
    
    def find(self, num, father):
        if father[num] == 0:
            return num
        father[num] = self.find(father[num], father)
        return father[num]

# 主函数
if __name__ == '__main__':
    conn = Connection("Acity","Bcity",1)
    conn1 = Connection("Acity","Ccity",2)
    conn2 = Connection("Bcity","Ccity",3)
    connections = [conn, conn1, conn2]
    s = Solution()
    ci01 = s.lowestCost(connections)[0].city1
    ci02 = s.lowestCost(connections)[0].city2
    co0 = s.lowestCost(connections)[0].cost
    ci11 = s.lowestCost(connections)[1].city1
    ci12 = s.lowestCost(connections)[1].city2
    ci1 = s.lowestCost(connections)[1].cost
    print("Output: ", [[ci01, ci02, co0],[ci11,ci12,ci1]])


# 运行结果
# Output:  [['Acity', 'Bcity', 1], ['Acity', 'Ccity', 2]]