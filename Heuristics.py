import numpy as np
from MazeProblem import MazeState, MazeProblem, compute_robot_direction
from Robot import UniformCostSearchRobot
from GraphSearch import NodesCollection


def tail_manhattan_heuristic(state: MazeState):
    # TODO (EX 7.2), implement heuristic, delete exception
    tx = abs(state.tail[0] - state.maze_problem.tail_goal[0])
    ty = abs(state.tail[1] - state.maze_problem.tail_goal[1])
    return (tx+ty) * state.maze_problem.forward_cost

def get_center(i1, i2):
    center = 0
    if i1 == i2:
        center = i1
    else:
        center = abs(i1+i2)//2 + 1
    return center

def center_manhattan_heuristic(state: MazeState):
    # TODO (EX 9.2), implement heuristic, delete exception
    center_state_x = get_center(state.head[0], state.tail[0])
    center_state_y = get_center(state.head[1], state.tail[1])
    center_maze_x = get_center(state.maze_problem.head_goal[0], state.maze_problem.tail_goal[0])
    center_maze_y = get_center(state.maze_problem.head_goal[1], state.maze_problem.tail_goal[1])
    res = abs(center_state_y - center_maze_y) + abs(center_state_x - center_maze_x)
    return res



class ShorterRobotHeuristic:
    def __init__(self, maze_problem: MazeProblem, k):
        assert k % 2 == 0, "odd must be even"
        assert maze_problem.length - k >= 3, f"it is not possible to shorten a {maze_problem.length}-length robot by " \
                                             f"{k} units because robot length has to at least 3"
        self.k = k
        ################################################################################################################
        # TODO (EX. 13.2): replace all three dots, delete exception
        raise NotImplemented
        shorter_robot_head_goal, shorter_robot_tail_goal = ...
        self.new_maze_problem = MazeProblem(maze_map=...,
                                            initial_head=...,
                                            initial_tail=...,
                                            head_goal=shorter_robot_head_goal,  # doesn't matter, don't change
                                            tail_goal=shorter_robot_tail_goal)  # doesn't matter, don't change        self.node_dists = ...().solve(..., compute_all_dists=True)
        ################################################################################################################

        assert isinstance(self.node_dists, NodesCollection)

    def _compute_shorter_head_and_tails(self, head, tail):
        # TODO (EX. 13.1): complete code here, delete exception
        raise NotImplemented

    def __call__(self, state: MazeState):
        # TODO (EX. 13.3): replace each three dots, delete exception
        raise NotImplemented
        shorter_head_location, shorter_tail_location = ...
        new_state = MazeState(..., head=..., tail=...)
        if new_state in self.node_dists:
            node = self.node_dists.get_node(new_state)
            return ...
        else:
            return ...  # what should we return in this case, so that the heuristic would be as informative as possible
                        # but still admissible
