from Robot import *
from MazeProblem import *
from Animation import Animation
from Heuristics import *
from Utilities import *
from Experiments import *


if __name__ == "__main__":

   # a = solve_and_display(BestFirstSearchRobot, 1, False)
   #  a = solve_and_display(UniformCostSearchRobot, 1, False)
    #test_robot(UniformCostSearchRobot, [0 ,1 ,2 ,3 ,4,5])
    test_robot(BreadthFirstSearchRobot, [0 ,1 ,2 ,3 ,4,5])
