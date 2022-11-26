from enum import Flag, auto
from dataclasses import dataclass


class TileType(Flag):
    FLOOR = auto()
    WALL = auto()


@dataclass
class Tile:
    type: TileType
