class Colors():
    def __init__(self, R, G, B):
        self.R = R
        self.G = G
        self.B = B

    def get_color(self):
        return (self.R, self.G, self.B)


TileFloorColor = Colors(192, 192, 192)
TileWallColor = Colors(0, 0, 0)
TileRoomColor = Colors(255, 248, 220)
BorderColors = Colors(128, 128, 128)
