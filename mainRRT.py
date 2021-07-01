import time

import pygame
from RRTbasePy import RRTGraph, RRTMap


def main():
    dimensions = (600,1000)
    stat = (50,50)
    goal = (510,510)
    obsdim = 30
    obsnum = 50
    itteration = 0

    pygame.init()
    map = RRTMap(stat,goal,dimensions,obsdim,obsnum)
    graph = RRTGraph(stat,goal,dimensions,obsdim,obsnum)

    obstacles = graph.makobs()
    map.drawMap(obstacles)
    '''
    while True:
        x,y = graph.sample_envir()
        n = graph.number_of_nodes()
        graph.add_node(n,x,y)
        graph.add_edge(n-1,n)
        x1,y1 = graph.x[n],graph.y[n]
        x2, y2 = graph.x[n-1], graph.y[n - 1]
        if(graph.isFree()):
            pygame.draw.circle(map.map,map.red,(graph.x[n],graph.y[n]),map.nodeRad,map.nodeThickness)
            if not graph.crossObstacle(x1,x2,y1,y2):
                pygame.draw.line(map.map,map.blue,(x1,y1),(x2,y2),map.edgeThickness)
        pygame.display.update()
        #pygame.event.clear()
        #pygame.event.wait(0)
    '''
    while (not graph.path_to_goal()):
        if itteration % 10 == 0:
            X,Y, Parent = graph.bias(goal)
            pygame.draw.circle(map.map, map.gray, (X[-1], Y[-1]), map.nodeRad + 2, 0)
            pygame.draw.line(map.map, map.blue, (X[-1], Y[-1]), (X[Parent[-1]], Y[Parent[-1]]), map.edgeThickness)
        else:
            X,Y,Parent = graph.expand()
            pygame.draw.circle(map.map, map.gray, (X[-1],Y[-1]),map.nodeRad+2,0)
            pygame.draw.line(map.map, map.blue, (X[-1], Y[-1]), (X[Parent[-1]], Y[Parent[-1]]), map.edgeThickness)

        if itteration % 5 == 0:
            pygame.display.update()
        itteration +=1
    time.sleep(0.1)
    map.drawPath(graph.getPathCoords())
    pygame.display.update()
    pygame.event.clear()
    pygame.event.wait()


if __name__ == '__main__':
    main()
