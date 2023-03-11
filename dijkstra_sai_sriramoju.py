import numpy as np
import cv2 
from queue import PriorityQueue

def shapes(map, image, clearance):
    ##hexagon##
    hexagon_vertices = [[300,125-75],[365,125-37],[365,125+37],[300,125+75],[300-65,125+37],[300-65,125-37]]
    hexagon_vertices = np.array(hexagon_vertices)
    map = cv2.fillPoly(map, [hexagon_vertices], color=255)
    map = cv2.polylines(map, [hexagon_vertices], isClosed=True, color=255, thickness=clearance-2)
    image = cv2.fillPoly(image, [hexagon_vertices], color=(255,255,0))
    image = cv2.polylines(image, [hexagon_vertices], isClosed=True, color=(255,255,255), thickness=clearance-2)

    ##rectangles##
    rectangle_vertices_1 = np.array([[100,0],[100,100],[150,100],[150,0]])
    map = cv2.fillPoly(map, [rectangle_vertices_1], color=255)
    map = cv2.polylines(map, [rectangle_vertices_1], isClosed=True, color=255, thickness=clearance-2)
    image = cv2.fillPoly(image, [rectangle_vertices_1], color=(255,255,0))
    image = cv2.polylines(image, [rectangle_vertices_1], isClosed=True, color=(255,255,255), thickness=clearance-2)

    rectangle_vertices_2 = np.array([[100,250],[100,150],[150,150],[150,250]])
    map = cv2.fillPoly(map, [rectangle_vertices_2], color=255)
    map = cv2.polylines(map, [rectangle_vertices_2], isClosed=True, color=255, thickness=clearance-2)
    image = cv2.fillPoly(image, [rectangle_vertices_2], color=(255,255,0))
    image = cv2.polylines(image, [rectangle_vertices_2], isClosed=True, color=(255,255,255), thickness=clearance-2)

    ##triangles##
    triangle_vertices = np.array([[460,125-100],[460,125+100],[510,125]])
    map = cv2.fillPoly(map, [triangle_vertices], color=255)
    map = cv2.polylines(map, [triangle_vertices], isClosed=True, color=255, thickness=clearance-2)
    image = cv2.fillPoly(image, [triangle_vertices], color=(255,255,0))
    image = cv2.polylines(image, [triangle_vertices], isClosed=True, color=(255,255,255), thickness=clearance-2)


    return image, map


def dijkstra_algo():
    pass

if __name__ == '__main__':
    map = np.zeros((250, 600))
    image = np.zeros((250, 600,3), dtype=np.uint8)
    clearance = 5
    img, map = shapes(map, image, clearance)
    cv2.imshow("Hexagon with Border", image)
    cv2.waitKey(0)


