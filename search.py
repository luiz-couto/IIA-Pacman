# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return [s, s, w, s, w, w, s, w]


def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """

    def runDfs(state, path, visited):
        children_states = problem.getSuccessors(state[0])
        for child in children_states:
            if (child[0] not in visited and child[0] != problem.getStartState()):

                if problem.isGoalState(child[0]):
                    return (True, path + [child[1]])

                reached_goal, childPath = runDfs(child, path + [child[1]], visited + [child[0]])
                if reached_goal:
                    return (True, childPath)
        
        return (False, path)

    _, path = runDfs((problem.getStartState(), '', 0), list(), list())
    return path


def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    
    final_path = []
    explored = []
    frontier = util.Queue()
    
    curr_state = problem.getStartState()
    frontier.push((curr_state, []))

    while True:
        if frontier.isEmpty():
            break
        
        curr_state, path = frontier.pop()

        if problem.isGoalState(curr_state):
            final_path = path
            break

        explored = explored + [curr_state]

        for child in problem.getSuccessors(curr_state):
            if child[0] not in explored:
                frontier.push((child[0], path + [child[1]]))
                explored = explored + [child[0]]

    return final_path



def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    
    final_path = []
    explored = []
    frontier = util.PriorityQueue()
    counter = util.Counter()
    
    curr_state = problem.getStartState()
    
    frontier.push((curr_state, [], 0), 0)
    counter[curr_state] = 1

    while True:
        if frontier.isEmpty():
            break
        
        curr_state, path, cost = frontier.pop()
        counter[curr_state] = 0

        if problem.isGoalState(curr_state):
            final_path = path
            break
        
        if curr_state in explored:
            continue

        explored = explored + [curr_state]

        for child in problem.getSuccessors(curr_state):
            updateCount = False
            if ((child[0] not in explored) and (counter[child[0]] == 0)):
                frontier.push((child[0], path + [child[1]], cost + child[2]), cost + child[2])
                updateCount = True
            
            if counter[child[0]] == 1:
                frontier.update((child[0], path + [child[1]], cost + child[2]), cost + child[2])
            
            if updateCount:
                counter[child[0]] = 1;
            

    return final_path



def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0


def greedySearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest heuristic first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


def foodHeuristic(state, problem):
    """
    Your heuristic for the FoodSearchProblem goes here.

    This heuristic must be consistent to ensure correctness.  First, try to come
    up with an admissible heuristic; almost all admissible heuristics will be
    consistent as well.

    If using A* ever finds a solution that is worse uniform cost search finds,
    your heuristic is *not* consistent, and probably not admissible!  On the
    other hand, inadmissible or inconsistent heuristics may find optimal
    solutions, so be careful.

    The state is a tuple ( pacmanPosition, foodGrid ) where foodGrid is a Grid
    (see game.py) of either True or False. You can call foodGrid.asList() to get
    a list of food coordinates instead.

    If you want access to info like walls, capsules, etc., you can query the
    problem.  For example, problem.walls gives you a Grid of where the walls
    are.

    If you want to *store* information to be reused in other calls to the
    heuristic, there is a dictionary called problem.heuristicInfo that you can
    use. For example, if you only want to count the walls once and store that
    value, try: problem.heuristicInfo['wallCount'] = problem.walls.count()
    Subsequent calls to this heuristic can access
    problem.heuristicInfo['wallCount']
    """
    position, foodGrid = state
    "*** YOUR CODE HERE ***"
    return 0


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
ucs = uniformCostSearch
gs = greedySearch
astar = aStarSearch
