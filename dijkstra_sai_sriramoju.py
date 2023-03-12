import numpy as np
import cv2 
from queue import PriorityQueue
import time
from collections import defaultdict

def shapes(map, image, clearance):
    ##hexagon##
    clearance = clearance+2
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

def validpoint(x,y,map):
    if map[y,x] == 0:
        return True
    else:
        return False

def MoveLeft(x,y,TempMap):
    if(0<= (x-1) <TempMap.shape[1] and (0 <= y < TempMap.shape[0])):
        if TempMap[y][x-1] == 0:
            return [x-1, y] , 1
    return None

def MoveRight(x,y,TempMap):
    if(0<= (x+1) <TempMap.shape[1] and (0 <= y < TempMap.shape[0])):
        if TempMap[y][x+1] == 0:
            return [x+1, y], 1
    return None

def MoveUp(x,y,TempMap):
    if(0<= x <TempMap.shape[1] and (0 <= (y+1) < TempMap.shape[0])):
        if TempMap[y+1][x] == 0:
            return [x, y+1], 1
    return None

def MoveDown(x,y,TempMap):
    if(0<= x <TempMap.shape[1] and (0 <= (y-1) < TempMap.shape[0])):
        if TempMap[y-1][x] == 0:
            return [x, y-1], 1
    return None

def MoveLeftDiagUp(x,y,TempMap):
    if(0<= (x-1) <TempMap.shape[1] and (0 <= (y+1) < TempMap.shape[0])):
        if TempMap[y+1][x-1] == 0:
            return [x-1, y+1], 1.4
    return None

def MoveLeftDiagDown(x,y,TempMap):
    if(0<= (x-1) <TempMap.shape[1] and (0 <= (y-1) < TempMap.shape[0])):
        if TempMap[y-1][x-1] == 0:
            return [x-1, y-1], 1.4
    return None

def MoveRightDiagUp(x,y,TempMap):
    if(0<= (x+1) <TempMap.shape[1] and (0 <= (y+1) < TempMap.shape[0])):
        if TempMap[y+1][x+1] == 0:
            return [x+1, y+1], 1.4
    return None

def MoveRightDiagDown(x,y,TempMap):
    if(0<= (x+1) <TempMap.shape[1] and (0 <= (y-1) < TempMap.shape[0])):
        if TempMap[y-1][x+1] == 0:
            return [x+1, y-1], 1.4
    return None

def get_new_nodes_cost(current_point, TempMap):
    costs = []
    nodes = []
    x = current_point[0]
    y = current_point[1]

    if MoveLeft(x,y,TempMap) != None:
        point, cost = MoveLeft(x,y,TempMap)
        costs.append(cost)
        nodes.append(point)
    if MoveRight(x,y,TempMap) != None:
        point, cost = MoveRight(x,y,TempMap)
        costs.append(cost)
        nodes.append(point)
    if MoveUp(x,y,TempMap) != None:
        point, cost = MoveUp(x,y,TempMap)
        costs.append(cost)
        nodes.append(point)
    if MoveDown(x,y,TempMap) != None:
        point, cost = MoveDown(x,y,TempMap)
        costs.append(cost)
        nodes.append(point)
    if MoveLeftDiagUp(x,y,TempMap) != None:
        point, cost = MoveLeftDiagUp(x,y,TempMap)
        costs.append(cost)
        nodes.append(point)
    if MoveLeftDiagDown(x,y,TempMap) != None:
        point, cost = MoveLeftDiagDown(x,y,TempMap)
        costs.append(cost)
        nodes.append(point)
    if MoveRightDiagUp(x,y,TempMap) != None:
        point, cost = MoveRightDiagUp(x,y,TempMap)
        costs.append(cost)
        nodes.append(point)
    if MoveRightDiagDown(x,y,TempMap) != None:
        point, cost = MoveRightDiagDown(x,y,TempMap)
        costs.append(cost)
        nodes.append(point)
    
    return costs, nodes

def backtracking(parents, start_point, end_point):

    path = []
    start_node = (start_point[0], start_point[1])
    i = (end_point[0],end_point[1])
    path.append(i)
    parent_nodes = list(parents.keys())
    children_nodes = list(parents.values())
    while True:
        for children in children_nodes:
            if i in children:
                x = children_nodes.index(children)
                path.append(parent_nodes[x])
                i = parent_nodes[x]
            if i == start_node:
                return path[::-1]

def dijkstra_algo(start, goal, map, C2C):
    open = PriorityQueue()
    closed = []
    C2C[start[1], start[0]] = 0
    open.put((0,start))
    parents = defaultdict(list)
    i = 0

    while not open.empty():
        _,current = open.get()
        if current not in closed:
            closed.append(current)

        if current == goal:
            print('Goal Reached!')
            break
        costs, nodes = get_new_nodes_cost(current, map)
        for (cost, node) in zip(costs, nodes):
            if node not in closed:
                temp_cost = C2C[current[1],current[0]] + cost
                if temp_cost < C2C[node[1],node[0]]:
                    C2C[node[1],node[0]] = temp_cost
                    parents[(current[0],current[1])].append((node[0], node[1]))
                    open.put((temp_cost, node))
    return closed, parents, current

if __name__ == '__main__':
    map = np.zeros((250, 600))
    image = np.zeros((250, 600,3), dtype=np.uint8)
    CostToCome = np.full_like(map, np.inf)
    clearance = 5
    img, map = shapes(map, image, clearance)
    CostToCome[map!=0] = -1

    while True:
        print('Enter the start points as x,y: ')
        points_start = input()
        x_start = int(points_start.split(",")[0])
        y_start = int(points_start.split(",")[1])
        
        print('Enter the goal points as x,y: ')
        points_goal = input()
        x_goal = int(points_goal.split(",")[0])
        y_goal = int(points_goal.split(",")[1])
        
        try:
            if validpoint(x_start,y_start, map) and validpoint(x_goal,y_goal, map):
                break
            else:
                print("Please enter the points which are in free space!")
                continue
        except:
            print("Dimensions more than the given map, try again!")

    a = time.time()
    start = [x_start, y_start]
    end = [x_goal, y_goal]
    closed, parents, last_node = dijkstra_algo(start, end, map, CostToCome)
    path = backtracking(parents, start, last_node)
    b = time.time()
    print("time taken to explore from ("+str(start[0]) +","+ str(start[1])+") to ("+str(end[0])+","+str(end[1])+") is "+ str(b-a)+ "seconds")
    # print(path)
    # print(closed)
    closed_len = len(closed)
    path_len = len(path)
    final = closed+path
    i = 0
    fourcc = cv2.VideoWriter_fourcc(*'MJPG')
    video = cv2.VideoWriter("dijkstra_demonstration.avi", fourcc, 100, (image.shape[1], image.shape[0]))
    
    for points1 in final:
        if i<closed_len:
            image[points1[1], points1[0]] = (0,255,0)
        else:
            image[points1[1], points1[0]] = (0,0,0)
            time.sleep(0.1)
        temp_image = image[::-1,:,:]
        i += 1
        video.write(temp_image)
        cv2.imshow("Dijkstra", temp_image)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cv2.imwrite('Shortest_distance_trajectory.jpg', temp_image)
    cv2.imshow("Dijkstra",temp_image)
    cv2.waitKey(0)
 