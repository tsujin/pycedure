import numpy as np

tile_dt = np.dtype([
    ("walkable", np.bool),
    ("transparent", np.bool)
])

def create_tile(
        walkable: int,
        transparent: int
) -> np.ndarray:
    return np.array((walkable, transparent), dtype=tile_dt)

floor = create_tile(walkable=True, transparent=True)
wall = create_tile(walkable=False, transparent=False)