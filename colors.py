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
TileWeaponColor = Colors(125, 125, 125)
TileCharacterColor = Colors(0, 255, 0)
BorderColors = Colors(128, 128, 128)
Yellow = Colors(255,255,0)
Pink = Colors(255, 192, 203)
Red = Colors(255,0,0)
Green = Colors(0,255,0)
Blue = Colors(0,0,255)
Purple = Colors(160,32,240)


