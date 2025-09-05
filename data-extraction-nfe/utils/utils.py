import numpy as np

def polygon_to_bbox(polygon):
    bbox = []
    for p in polygon:
        bbox.append([p.x, p.y])

    return np.array(bbox)