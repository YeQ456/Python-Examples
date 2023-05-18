# 问题描述
# 工厂模式是一个常见的设计模式，实现一个玩具工厂ToyFactory，用于生产不同的玩具类型。
# 假设只有猫和狗两种玩具


# 示例
# 输入：ToyFactory tf = ToyFactory()
#      Toy toy = tf.getToy('Dog')
#       toy.talk()
# 输出： Wow

# 输入：ToyFactory tf = ToyFactory()
#      Toy toy = tf.getToy('Cat')
#       toy.talk()
# 输出： Meow


# 源码实现
class Toy:
    def talk(self):
        raise NotImplementedError('This method should have implemented.')

class Dog(Toy):
    def talk(self):
        print("Wow")

class Cat(Toy):
    def talk(self):
        print("Meow")

class ToyFactory:
    def getToy(self, type):
        if type == 'Dog':
            return Dog()
        elif type == 'Cat':
            return Cat()
        
        return None

# 主函数
if __name__ == '__main__':
    ty = ToyFactory()
    type = 'Dog'
    type1 = 'Cat'
    toy = ty.getToy(type)    
    print("Input: type = Dog, Output: ")
    toy.talk()
    toy = ty.getToy(type1)
    print("Input: type = Cat, Output: ")
    toy.talk()



# 运行结果
# Input: type = Dog, Output: 
# Wow
# Input: type = Cat, Output:
# Meow