
from mcts_node import MCTSNode
from p2_t3 import Board
from random import choice
from math import sqrt, log

num_nodes = 100
explore_faction = 2.

def traverse_nodes(node: MCTSNode, board: Board, state, bot_identity: int):
    """ Traverses the tree until the end criterion are met.
    e.g. find the best expandable node (node with untried action) if it exist,
    or else a terminal node

    Args:
        node:       A tree node from which the search is traversing.
        board:      The game setup.
        state:      The state of the game.
        identity:   The bot's identity, either 1 or 2

    Returns:
        node: A node from which the next stage of the search can proceed.
        state: The state associated with that node

    """
    best_child = node
    top_UCB = 0
    new_state = state

    for child in node.child_nodes:
        cur_child = node.child_nodes[child]
        UCB = ucb(cur_child, False)
        if UCB >= top_UCB:
            top_UCB = UCB
            best_child = cur_child
    
    if best_child.parent_action != None:
        new_state = board.next_state(state, best_child.parent_action)
    return best_child, new_state

def expand_leaf(node: MCTSNode, board: Board, state):
    """ Adds a new leaf to the tree by creating a new child node for the given node (if it is non-terminal).

    Args:
        node:   The node for which a child will be added.
        board:  The game setup.
        state:  The state of the game.

    Returns:
        node: The added child node
        state: The state associated with that node

    """
    if node.untried_actions:
        # Select an untried action
        action = node.untried_actions.pop()
        
        # Ensure the action is legal
        if board.is_legal(state, action):
            # Create a new child node
            new_node = MCTSNode(parent=node, parent_action=action, action_list=board.legal_actions(board.next_state(state, action)))
            node.child_nodes[action] = new_node
            
            # Update the current state based on the selected action
            state = board.next_state(state, action)
            
            return new_node, state

    return node, state



def rollout(board: Board, state):
    """ Given the state of the game, the rollout plays out the remainder randomly.

    Args:
        board:  The game setup.
        state:  The state of the game.
    
    Returns:
        state: The terminal game state

    """
    # while(state.legal_moves!=[]):    
    #     state.apply_move(choice(state.legal_moves))
    while board.legal_actions(state) != []:
        moves = board.legal_actions(state)
        state = board.next_state(state, choice(moves))
    return state




def backpropagate(node: MCTSNode|None, won: bool):
    """ Navigates the tree from a leaf node to the root, updating the win and visit count of each node along the path.

    Args:
        node:   A leaf node.
        won:    An indicator of whether the bot won or lost the game.

    """
    while node:
        node.visits += 1
        if won:
            node.wins += 1
        node = node.parent


def ucb(node: MCTSNode, is_opponent: bool):
    """ Calcualtes the UCB value for the given node from the perspective of the bot

    Args:
        node:   A node.
        is_opponent: A boolean indicating whether or not the last action was performed by the MCTS bot
    Returns:
        The value of the UCB function for the given node
    """
    if node.visits == 0:
        return 0
    if is_opponent:
        exploit = node.wins / node.visits
        explore = explore_faction * sqrt(2 * log(node.parent.visits) / node.visits)
    else:
        exploit = node.wins / node.visits
        explore = explore_faction * sqrt(2 * log(node.visits) / node.visits)
    UCB = exploit + explore
    return UCB

def get_best_action(root_node: MCTSNode):
    """ Selects the best action from the root node in the MCTS tree

    Args:
        root_node:   The root node
    Returns:
        action: The best action from the root node
    
    """
    best = float("-inf")
    best_action = None
    for child in root_node.child_nodes:
        cur_child = root_node.child_nodes[child]
        if cur_child.wins >= best:
            best = cur_child.wins
            best_action = cur_child.parent_action
    return best_action


def is_win(board: Board, state, identity_of_bot: int):
    # checks if state is a win state for identity_of_bot
    outcome = board.points_values(state)
    assert outcome is not None, "is_win was called on a non-terminal state"
    return outcome[identity_of_bot] == 1

def think(board: Board, current_state):
    """ Performs MCTS by sampling games and calling the appropriate functions to construct the game tree.

    Args:
        board:  The game setup.
        current_state:  The current state of the game.

    Returns:    The action to be taken from the current state

    """
    bot_identity = board.current_player(current_state) # 1 or 2
    root_node = MCTSNode(parent=None, parent_action=None, action_list=board.legal_actions(current_state))

    for _ in range(num_nodes):
        state = current_state
        node = root_node
        # Do MCTS - This is all you!
        # ...

        sim_state = tuple(state)
        # Selection Step
        while node.untried_actions == [] and node.child_nodes != {}:
            node.visits += 1
            node, sim_state = traverse_nodes(node, board, sim_state, bot_identity)

        # Expansion Step
        node, state = expand_leaf(node, board, sim_state)

        # Simulation Step
        state = rollout(board, state)
        if is_win(board, state, bot_identity):
            won = True
        else:
            won = False

        # Backpropogation Step
        backpropagate(node, won)


    # Return an action, typically the most frequently used action (from the root) or the action with the best
    # estimated win rate.
    best_action = get_best_action(root_node)
    
    print(f"Action chosen: {best_action}")
    return best_action
