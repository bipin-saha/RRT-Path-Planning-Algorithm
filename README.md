# Rapidly Exploring Random Trees (RRT) Path Planning Algorithm

## Introduction
The **Rapidly Exploring Random Trees (RRT)** algorithm is a widely used path planning algorithm in robotics and autonomous systems. It is designed to find feasible paths for a robot or agent in a complex and often dynamic environment. The primary objective of the RRT algorithm is to efficiently explore the configuration space to connect a starting point to a goal point while avoiding obstacles.

## [YouTube](https://www.youtube.com/watch?v=OnCe3VK2WyI)

## RRT Components

### `RRTMap` Class
The `RRTMap` class is responsible for visualizing the map, including the start and goal points, obstacles, and the planned path. Here are the key functions and properties of this class:

- **Initialization**: Initializes the map and sets up the display window using Pygame.

- **drawMap**: Draws the initial map with the start, goal, and obstacles.

- **drawPath**: Draws the computed path on the map.

- **drawObs**: Draws obstacles on the map.

### `RRTGraph` Class
The `RRTGraph` class is responsible for managing the RRT tree and performing the core path planning operations. Here are the key functions and properties of this class:

- **Initialization**: Initializes the RRT tree with the start and goal points.

- **makeRandomRect**: Generates random obstacle rectangles within the map dimensions.

- **makobs**: Generates a set of random obstacles, ensuring they do not overlap with the start or goal positions.

- **add_node** and **remove_node**: Add and remove nodes (points) from the RRT tree.

- **add_edge** and **remove_edge**: Add and remove edges (connections) between nodes in the RRT tree.

- **distance**: Calculates the Euclidean distance between two nodes.

- **sample_envir**: Samples a random point within the map.

- **nearest**: Finds the nearest node in the RRT tree to a given point.

- **isFree**: Checks if a newly added node collides with any obstacles.

- **crossObstacle**: Determines if an edge between two points crosses any obstacles.

- **connect**: Attempts to connect two nodes by adding an edge if no obstacle is in the way.

- **step**: Moves from the nearest node towards a random sample within a specified distance.

- **path_to_goal**: Traces the path from the goal node back to the start node once the goal is reached.

- **getPathCoords**: Retrieves the coordinates of the nodes along the computed path.

- **bias**: Expands the RRT tree biased towards the goal.

- **expand**: Expands the RRT tree in a random direction.

### Main Algorithm
The `main` function coordinates the execution of the RRT algorithm. It sets up the map, initializes the RRT tree, generates random obstacles, and performs iterations of the RRT algorithm to connect the start and goal points.

The main loop alternates between two types of iterations:

1. **Biasing**: In every 10th iteration, the algorithm attempts to move towards the goal by biasing the exploration.
2. **Expanding**: In other iterations, the algorithm randomly expands the tree.

The algorithm continues until it successfully reaches the goal or exhausts a predefined number of iterations.

## Execution
To execute the RRT path planning algorithm, run the `mainRRT.py` script. It will visualize the process of RRT exploration, showing the start, goal, obstacles, and the computed path on the map.

In summary, the RRT algorithm is a versatile and widely used approach for path planning in robotics and other autonomous systems. It efficiently explores the configuration space to find feasible paths while avoiding obstacles, making it suitable for various real-world applications.
