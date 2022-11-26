import numpy as np
from Tile import Tile, TileType


class Map:
    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.tiles = np.full((width, height), fill_value=Tile(TileType.FLOOR), order='F')

    def __getitem__(self, item):
        return self.tiles[item]


m = Map(5, 5)
print(m[1][2])