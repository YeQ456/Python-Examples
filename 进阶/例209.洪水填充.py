# 问题描述
# 用一个2D整数数组表示一张图片，数组中每一个整数(0~65535)代表图片的像素行和列坐标。给定一个坐标(sr,sc)
# 代表洪水填充的起始像素，同时给定一个像素颜色newColor，"洪水填充"整张图片。
# 为了实现"洪水填充"，从起始像素点开始，将与起始像素颜色相同的4向连接的像素都填充为新颜色，然后将
# 与填充成新颜色的像素4向相连的、与起始像素颜色相同的像素也填充为新颜色....以此类推。返回修改后的图片


# 示例
# 输入：image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, newColor = 2
# 输出：[[2,2,2],[2,2,0],[2,0,1]]


# 源码实现
class Solution(object):
    def floorFill(self, image, sr, sc, newColor):
        rows, cols, orig_color = len(image), len(image[0]), image[sr][sc]
        def traverse(row, col):
            if(not (0 <= row < rows and 0 <= col < cols)) or image[row][col] != orig_color:
                return
            image[row][col] = newColor
            [traverse(row + x, col + y) for (x,y) in ((0,1),(1,0),(0,-1),(-1,0))]
        if orig_color != newColor:
            traverse(sr,sc)
        return image

if __name__ == '__main__':
    s = Solution()
    image = [[1,1,1],[1,1,0],[1,0,1]]
    sr = 1
    sc = 1
    newColor = 2
    print("输入图像：", image)
    print("输入坐标：", "[",sr,",",sc,"]")
    print("输入颜色：", newColor)
    print("输出：", (s.floorFill(image, sr,sc,newColor)))


# 运行结果
# 输入图像： [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
# 输入坐标： [ 1 , 1 ]
# 输入颜色： 2
# 输出： [[2, 2, 2], [2, 2, 0], [2, 0, 1]]