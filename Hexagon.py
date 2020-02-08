# screen size
S_HIGHT = 500
S_WIDTH = 500

# 正六角形クラス
class Hexagon:
    '''
        ----
       /    \
       \    /
        ----
    '''
    size = 40

    def __init__(self, x, y, color, wall):
        self.width = Hexagon.size
        self.height = Hexagon.size * 3 // 4
        pos_x = self.size // 3
        pos_y = S_HIGHT * 2 // 3
        tmp_x = pos_x + self.width * 2 // 3 * x
        tmp_y = pos_y - self.height * y + self.height // 2 * x
        vertexes_offset = [[0, 0], [self.width//3, 0], [self.width*2//3, -self.height//2], [self.width//3, -self.height], [0, -self.height], [-self.width//3, -self.height//2]]
        self.vertexes = [None]*6
        for i in range(6):
            self.vertexes[i] = [tmp_x+vertexes_offset[i][0], tmp_y+vertexes_offset[i][1]]
        self.x = x
        self.y = y
        self.color = color
        self.wall = wall
        self.active = True
        self.point = 1

    def find_coordinates(self, c_x, c_y, v1, v2):
        # y = ax + b ; x = (y - b) / a
        a = (v1[1] - v2[1]) / (v1[0] - v2[0])
        b = v1[1] - (a * v1[0])
        return [(c_y - b) / a, c_y]

    def is_in_area(self, c_x, c_y):
        d_y = self.vertexes[0][1] # yの最大値（下）
        u_y = self.vertexes[3][1] # yの最小値（上）
        l_x = self.vertexes[5][0] # xの最小値（左）
        r_x = self.vertexes[2][0] # xの最大値（右）
        #print(d_y, u_y, l_x, r_x)
        if c_y > d_y or c_y < u_y:
            return False
        elif c_x > r_x or c_x < l_x:
            return False
        else:
            pass
            # 正六角形内かを判定する処理を記述予定
        return True
