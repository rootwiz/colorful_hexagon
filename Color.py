import random

# 色クラス
class Color:
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    WALL_COLOR = WHITE
    INACTIVE_COLOR = WHITE
    NEUTRAL_COLOR = BLACK

    def __init__(self, n):
        #random.randrange(256)
        self.n = n
        self.colors = []
        for i in range(self.n-1):
            r = random.randrange(256)
            g = random.randrange(256)
            b = random.randrange(256)
            self.colors.append([r, g, b])
        self.counts = [0] * (self.n-1)

    def get_color_at(self, num):
        self.counts[num] += 1
        return self.colors[num]

    def get_color(self):
        tmp_l = list(range(self.n-1))
        random.shuffle(tmp_l)
        ret = False
        for item in tmp_l:
            if self.counts[item] >= 3*(self.n-2):
                continue
            else:
                self.counts[item] += 1
                ret = self.colors[item]
                break
        if ret == False:
            #ret = Color.BLACK
            ret = Color.NEUTRAL_COLOR
        return ret

    @staticmethod
    def random_color():
        r = random.randrange(256)
        g = random.randrange(256)
        b = random.randrange(256)
        return [r, g, b]
