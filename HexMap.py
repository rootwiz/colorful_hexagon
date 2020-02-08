import pygame
from pygame.locals import *
from Hexagon import Hexagon
from Color import Color

# screen size
S_HIGHT = 500
S_WIDTH = 500

# 盤面クラス
class HexMap:
    def __init__(self, n):
        self.n = n
        self.size = Hexagon.size
        self.width = self.size
        self.height = self.size * 3 // 4
        # 正六角形の左下の頂点から反時計回りに座標を取得する際のオフセット
        self.vertexes_offset = [[0, 0], [self.width//3, 0], [self.width*2//3, -self.height//2], [self.width//3, -self.height], [0, -self.height], [-self.width//3, -self.height//2]]
        self.hexagons = []
        self.rank = []
        self.coordinate_offset = [[1, 1], [1, 0], [0, -1], [-1, -1], [-1, 0], [0, 1]]
        self.vertex_index = {}
        colors = Color(n)
        k = self.n - 1
        l = 0
        ct = 0
        for i in range(2*n-1):  # x成分
            if i < n:
                k += 1
            else:
                l += 1
            for j in range(l, k):  # y成分
                if i == 0 or i == 2*n-2 or j == 0 or j == 2*n-2 or j == l or j == k-1:
                    self.hexagons.append(Hexagon(i, j, Color.WALL_COLOR, True))
                else:
                    self.hexagons.append(Hexagon(i, j, colors.get_color(), False))
                self.vertex_index[(i, j)] = ct
                ct += 1

    def draw(self):
        screen = pygame.display.set_mode((S_HIGHT+10, S_WIDTH+10))
        pygame.display.set_caption("Colorfull Hexagon")
        pos_x = self.size // 3
        pos_y = S_HIGHT * 2 // 3
        for hex in self.hexagons:
            tmp_x = pos_x + self.width * 2 // 3 * hex.x
            tmp_y = pos_y - self.height * hex.y + self.height // 2 * hex.x
            vertexes = [None]*6
            for i in range(6):
                vertexes[i] = [tmp_x+self.vertexes_offset[i][0], tmp_y+self.vertexes_offset[i][1]]
            pygame.draw.polygon(screen, hex.color, vertexes)

    def is_stable(self, x, y):
        cur_index = self.vertex_index[(x, y)]
        # 外壁のとき
        if self.hexagons[cur_index].wall == True:
            return True
        sur_coordinates = list(map(lambda l: ((x+l[0]), (y+l[1])), self.coordinate_offset))
        sur_indexes = list(map(lambda s: self.vertex_index[s], sur_coordinates))
        # 安定系1
        if self.hexagons[sur_indexes[0]].active == True and self.hexagons[sur_indexes[3]].active == True:
            return True
        # 安定系2
        elif self.hexagons[sur_indexes[1]].active == True and self.hexagons[sur_indexes[4]].active == True:
            return True
        # 安定系3
        elif self.hexagons[sur_indexes[2]].active == True and self.hexagons[sur_indexes[5]].active == True:
            return True
        # 安定系4
        elif self.hexagons[sur_indexes[0]].active == True and self.hexagons[sur_indexes[2]].active == True and self.hexagons[sur_indexes[4]].active == True:
            return True
        # 安定系5
        elif self.hexagons[sur_indexes[1]].active == True and self.hexagons[sur_indexes[3]].active == True and self.hexagons[sur_indexes[5]].active == True:
            return True
        # 不安定
        else:
            return False

    def judge_at(self, x, y):
        cur_index = self.vertex_index[(x, y)]
        cur_hexagon = self.hexagons[cur_index]
        if cur_hexagon.wall == True:
            return
        elif cur_hexagon.active == False:
            return
        if self.is_stable(x, y) == True:
            print(True)
            pass
        else:
            tmp_index = self.vertex_index[(x, y)]
            self.hexagons[tmp_index].color = Color.INACTIVE_COLOR
            self.hexagons[tmp_index].active = False
            print(False)

    def judge_all(self, x, y):
        research_vertexes = [(x, y)]
        print(research_vertexes)
        tmp_index = self.vertex_index[(x, y)]
        self.hexagons[tmp_index].color = Color.INACTIVE_COLOR
        self.hexagons[tmp_index].active = False
        self.draw()
        for offs in self.coordinate_offset:
            cur_x = x + offs[0]
            cur_y = y + offs[1]
            if self.is_stable(cur_x, cur_y) == True:
                print(True)
                pass
            else:
                tmp_index = self.vertex_index[(cur_x, cur_y)]
                self.hexagons[tmp_index].color = Color.INACTIVE_COLOR
                self.hexagons[tmp_index].active = False
                if self.hexagons[tmp_index].wall == True:
                    continue
                research_vertexes.append((cur_x, cur_y))
                print(False)

        while True:
            print(research_vertexes)
            if not research_vertexes:
                self.draw()
                break
            cur_coor = research_vertexes.pop()
            cur_index = self.vertex_index[cur_coor]
            cur_hexagon = self.hexagons[cur_index]
            if cur_hexagon.wall == True:
                continue
            elif cur_hexagon.active == False:
                continue
            elif self.is_stable(x, y) == True:
                print("stable")
                continue
            else:
                tmp_index = self.vertex_index[(x, y)]
                self.hexagons[tmp_index].color = Color.INACTIVE_COLOR
                self.hexagons[tmp_index].active = False
                print(False)
            for offs in self.coordinate_offset:
                cur_x = x + offs[0]
                cur_y = y + offs[1]
                if self.is_stable(cur_x, cur_y) == True:
                    print(True)
                    pass
                else:
                    tmp_index = self.vertex_index[(cur_x, cur_y)]
                    self.hexagons[tmp_index].color = Color.INACTIVE_COLOR
                    self.hexagons[tmp_index].active = False
                    if self.hexagons[tmp_index].wall == True:
                        continue
                    research_vertexes.append((cur_x, cur_y))
                    print(False)
            #time.sleep(1)
            self.draw()


    def cpos_to_ipos(self, click_x, click_y):
        i_x = 0
        i_y = 0
        for hex in self.hexagons:
            if hex.is_in_area(click_x, click_y):
                i_x = hex.x
                i_y = hex.y
                break
        return (i_x, i_y)
