import Heuristics
import MazeProblem
from Robot import *
from MazeProblem import *
from Animation import Animation
from Heuristics import *
from Utilities import *
from Experiments import *


if __name__ == "__main__":

    a = solve_and_display(WAStartRobot, 4, False, heuristic = tail_manhattan_heuristic)
     # a = solve_and_display(UniformCostSearchRobot, 1, False)
    #test_robot(UniformCostSearchRobot, [0 ,1 ,2 ,3 ,4,5])
    # test_robot(WAStartRobot, [0 ,1 ,2 ,3 ,4,5], heuristic = tail_manhattan_heuristic)
    # test_robot(BreadthFirstSearchRobot, [1 ,3 ])
   # test_robot(UniformCostSearchRobot, [1 ,3 ])
