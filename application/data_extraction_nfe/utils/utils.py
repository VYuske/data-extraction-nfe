import numpy as np

def polygon_to_bbox(polygon):
    bbox = []
    for p in polygon:
        bbox.append([p.x, p.y])

    return np.array(bbox)

def detection_array_to_dictionary(detection):
    url = detection.data.decode('utf-8')
    type = detection.type
    bbox = polygon_to_bbox(detection.polygon)

    return {
        'url': url,
        'type': type,
        'bbox': bbox
    }