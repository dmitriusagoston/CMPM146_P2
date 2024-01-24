# People
- Dmitrius Agoston
- Vincent Kuniadjaja

# Modifications to mcts_modified.py
In addition to the original implementation of MCTS, instead of selecting the node with the highest win rate, we calculated a heuristic using the minmax algorithm, in which each node would return the heuristic of 0.8 * average_winrate_or_all_children + 0.2 * max_winrate, and selecting the best heuristic. The reason for this is that the search would select nodes that are generally the best outcome rather than select the node with the single best outcome in order to make the bot make more consistent, safer plays.
