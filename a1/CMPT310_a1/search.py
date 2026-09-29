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
from game import Directions
from typing import List

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




def tinyMazeSearch(problem: SearchProblem) -> List[Directions]:
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem: SearchProblem) -> List[Directions]:
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
    "*** YOUR CODE HERE ***"

    #1. create stack
    #2. add start pos to stack 
    #3. while loop until fringe is empty
    #4. pop top element off stack and form path
    #5. if not goal state, add successors from right to left with path
    #4. return to top of while loop

    stack = util.Stack() #stack for traversal
    start_pos = problem.getStartState() #get the starting state
    stack_item = [start_pos, []] #push the start state and an empty path for the first node
    stack.push(stack_item)

    visited_states=[] #will store visited states so we don't repeatedl visit states

    while not stack.isEmpty(): #keep searching until the fringe is empty
        stack_top = stack.pop()
        state = stack_top[0]
        path = stack_top[1]
        if problem.isGoalState(state): #return path if we have reached the end
            return path
        elif state not in visited_states: #add state to visited states list to prevent visiting repeated states
            visited_states.append(state)
        else:
            continue
        successors = problem.getSuccessors(state) #get successors of current state
        for element in successors: #push the new states 
            new_path = path.copy()
            new_path.append(element[1])
            stack_item = [element[0],new_path] 
            stack.push(stack_item)

            ##code to run
            #python3 pacman.py -l tinyMaze -p SearchAgent
            #python3 pacman.py -l mediumMaze -p SearchAgent
            #python3 pacman.py -l bigMaze -z .5 -p SearchAgent



 

    util.raiseNotDefined()

def breadthFirstSearch(problem: SearchProblem) -> List[Directions]:
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"

    queue = util.Queue() #use a queue for traversal
    start_pos = problem.getStartState() #get the starting state
    queue_item = [start_pos,[]] #push the start state and an empty path for the first node
    queue.push(queue_item)

    visited_states = [] #will contain visited states to avoid repeating nodes

    while not queue.isEmpty(): #keep searching until the fringe is empty
        queue_front = queue.pop()
        state = queue_front[0]
        path = queue_front[1]
        if problem.isGoalState(state):
            return path
        elif state not in visited_states:
            visited_states.append(state)
        else:
            continue
        successors = problem.getSuccessors(state)
        for element in successors:
            new_path = path.copy()
            new_path.append(element[1])
            new_queue_item = [element[0],new_path]
            queue.push(new_queue_item)

            #code to run
            # python3 pacman.py -l mediumMaze -p SearchAgent -a fn=bfs
            # python3 pacman.py -l bigMaze -p SearchAgent -a fn=bfs -z .5


    
    util.raiseNotDefined()

def uniformCostSearch(problem: SearchProblem) -> List[Directions]:
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"

    queue = util.PriorityQueue()
    start_pos = problem.getStartState()
    queue_item = [start_pos,[],0] 
    queue.push(queue_item,0)

    visited_states = [] #will contain visited states to avoid repeating nodes

    while not queue.isEmpty():
        queue_front=queue.pop()
        state=queue_front[0]
        path=queue_front[1]
        cost=queue_front[2]
        if problem.isGoalState(state):
            return path
        elif state not in visited_states:
            visited_states.append(state)
        else:
            continue
        successors = problem.getSuccessors(state)
        for element in successors:
            new_path=path.copy()
            new_path.append(element[1])
            new_cost=cost+element[2]
            new_queue_item=[element[0],new_path,new_cost]
            queue.push(new_queue_item,new_cost)

    #code to run
    # python3 pacman.py -l mediumMaze -p SearchAgent -a fn=ucs
    # python3 pacman.py -l mediumDottedMaze -p StayEastSearchAgent
    # python3 pacman.py -l mediumScaryMaze -p StayWestSearchAgent


    util.raiseNotDefined()

def nullHeuristic(state, problem=None) -> float:
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """

    return 0

def aStarSearch(problem: SearchProblem, heuristic=nullHeuristic) -> List[Directions]:
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"

    queue = util.PriorityQueue()
    start_pos = problem.getStartState()
    starting_f = heuristic(start_pos, problem)
    queue_item = [start_pos,[],0,heuristic(start_pos,problem)]  #store state, path, cost, heuristic
    queue.push(queue_item,starting_f)

    visited_dict = {}

    while not queue.isEmpty():
        queue_front=queue.pop()
        state=queue_front[0]
        path=queue_front[1]
        cost=queue_front[2]
        h = queue_front[3]
        if problem.isGoalState(state):
            return path
        elif state not in visited_dict:
            visited_dict[state]=cost
        else:
            if visited_dict[state] > cost:
                visited_dict[state] = cost
            else:
                continue
        successors = problem.getSuccessors(state)
        for element in successors:
            new_path=path.copy()
            new_path.append(element[1])
            new_cost=cost+element[2]
            new_h = heuristic(element[0],problem)
            f = new_cost+new_h
            new_queue_item=[element[0],new_path,new_cost,new_h]
            queue.push(new_queue_item,f)


        

    




    util.raiseNotDefined()

# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
