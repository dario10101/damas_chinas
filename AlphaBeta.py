import math
        
def max_value(state,game, alpha, beta, profundidad):
    profundidad +=1
    if game.terminal_test(state,profundidad):
        return game.utility(state)
    v = -math.inf
    for a in game.actions(state,1):
        v = max(v, min_value(a,game, alpha, beta, profundidad))
        if v >= beta:
            return v
        alpha = max(alpha, v)
    return v

def min_value(state,game, alpha, beta, profundidad):
    profundidad += 1
    if game.terminal_test(state,profundidad):
        return game.utility(state)
    v = math.inf
    for a in game.actions(state):
        v = min(v, max_value(a,game, alpha, beta, profundidad))
        if v <= alpha:
            return v
        beta = min(beta, v)
    return v
    
def alphabeta_search(state, game):
        best_score = -math.inf
        beta = math.inf
        profundidad = 0
        best_action = None
        for a in game.actions(state,1):
            v = min_value(a,game, best_score, beta, profundidad)
            if v > best_score:
                best_score = v
                best_action = a
        return best_action
