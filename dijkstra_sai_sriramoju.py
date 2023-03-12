import numpy as np
import cv2 
from queue import PriorityQueue
import time
from collections import defaultdict

def shapes(map, image, clearance):
    ##hexagon##
    hexagon_vertices = [[300,50],[365,88],[365,162],[300,200],[235,162],[235,88]]
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


def MoveLeft(x,y,TempMap):
    if(0<= (x-1) <TempMap.shape[1] and (0 <= y < TempMap.shape[0])):
        if TempMap[x-1,y] == 0:
            return [x-1, y] , 1
    return None

def MoveRight(x,y,TempMap):
    if(0<= (x+1) <TempMap.shape[1] and (0 <= y < TempMap.shape[0])):
        if TempMap[x+1,y] == 0:
            return [x+1, y], 1
    return None

def MoveUp(x,y,TempMap):
    if(0<= x <TempMap.shape[1] and (0 <= (y+1) < TempMap.shape[0])):
        if TempMap[x,y+1] == 0:
            return [x, y+1], 1
    return None

def MoveDown(x,y,TempMap):
    if(0<= x <TempMap.shape[1] and (0 <= (y-1) < TempMap.shape[0])):
        if TempMap[x,y-1] == 0:
            return [x, y-1], 1
    return None

def MoveLeftDiagUp(x,y,TempMap):
    if(0<= (x-1) <TempMap.shape[1] and (0 <= (y+1) < TempMap.shape[0])):
        if TempMap[x-1,y+1] == 0:
            return [x-1, y+1], 1.4
    return None

def MoveLeftDiagDown(x,y,TempMap):
    if(0<= (x-1) <TempMap.shape[1] and (0 <= (y-1) < TempMap.shape[0])):
        if TempMap[x-1,y-1] == 0:
            return [x-1, y-1], 1.4
    return None

def MoveRightDiagUp(x,y,TempMap):
    if(0<= (x+1) <TempMap.shape[1] and (0 <= (y+1) < TempMap.shape[0])):
        if TempMap[x+1,y+1] == 0:
            return [x+1, y+1], 1.4
    return None

def MoveRightDiagUp(x,y,TempMap):
    if(0<= (x+1) <TempMap.shape[1] and (0 <= (y-1) < TempMap.shape[0])):
        if TempMap[x+1,y-1] == 0:
            return [x+1, y-1], 1.4
    return None



def dijkstra_algo(start, goal, map, image, C2C):
    open = PriorityQueue()
    closed = []
    C2C[start[0],start[1]] = 0
    open.put(0,start)
    parent = defaultdict(list)

    while True:
        dummy,current = open.get()
        if current not in closed:
            closed.append(current)
        
        if current == goal:
            print('Goal Reached!')
        
        

if __name__ == '__main__':
    map = np.zeros((250, 600))
    image = np.zeros((250, 600,3), dtype=np.uint8)
    CostToCome = np.full_like(map, np.inf)
    clearance = 5
    img, map = shapes(map, image, clearance)
    CostToCome[map!=0] = -1
    flip = img[::-1,:,:]
    cv2.imshow('frame', image)
    cv2.waitKey(0)

    


