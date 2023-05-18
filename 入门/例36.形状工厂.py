# 问题描述
# 实现一个形状工厂ShapeFactory创建不同的形状，假设只有三角形、正方形和矩形3种形状


# 示例
# 输入：
#       ShapeFactory sf = new ShapeFactory()
#       Shape shape = sf.getShape("Square")
#       shape.draw()
# 输出：
#        ----
#       |    |
#       |    |
#        ----

# 输入：
#       ShapeFactory sf = new ShapeFactory()
#       Shape shape = sf.getShape("Triangle")
#       shape.draw()
# 输出：
#       /\
#      /  \
#     /____\

# 输入：
#       ShapeFactory sf = new ShapeFactory()
#       Shape shape = sf.getShape("Rectangle")
#       shape.draw()
# 输出：
#       ----
#      |    |
#       ----


# 源码实现
class Shape:
    def draw(self):
        raise NotImplementedError('This method should have implemented.')

class Triangle(Shape):
    def draw(self):
        print('   /\\ ')
        print('  /  \\ ')
        print(' /____\\ ')

class Rectangle(Shape):
    def draw(self):
        print('  ----  ')
        print(' |    | ')
        print('  ----  ')

class Square(Shape):
    def draw(self):
        print('  ----  ')
        print(' |    | ')
        print(' |    | ')
        print('  ----  ')

class ShapeFactory:
    def getShape(self, shapeType):
        if shapeType == "Triangle":
            return Triangle()
        if shapeType == "Rectangle":
            return Rectangle()
        if shapeType == "Square":
            return Square()
        else:
            return None

# 主函数
if __name__ == '__main__':
    sf = ShapeFactory()
    shapeType = 'Triangle'
    shape = sf.getShape(shapeType)
    print("Input: type = Triangle, \nOutput: ")
    shape.draw()
    shapeType1 = 'Rectangle'
    shape = sf.getShape(shapeType1)
    print("Input: type = Rectangle, \nOutput: ")
    shape.draw()
    shapeType2 = 'Square'
    shape = sf.getShape(shapeType2)
    print("Input: type = Square, \nOutput: ")
    shape.draw()



# 运行结果
# Input: type = Triangle, 
# Output:
#    /\
#   /  \
#  /____\
# Input: type = Rectangle,
# Output:
#   ----
#  |    |
#   ----
# Input: type = Square,
# Output:
#   ----
#  |    |
#  |    |
#   ----