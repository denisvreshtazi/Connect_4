import utils
import random
import games

def h0(state, player):
    return random.randint(-100,100)

def h1(state, player):
    if (state.utility == 1):
        return state.utility*1000
    elif (state.utility == -1 ):
        return state.utility*1000
    return random.randint(-100,100)

def h2(state, player):

    enemy = plenemy(player)
    h = 0
    if (state.utility == 1):
        return state.utility * 1000
    elif(state.utility == -1):
        return state.utility * 1000

    for (x,y) in legal_moves(state):
        
       """ if x == 4:
            h -= 10
        elif x == 3 or x == 5:
            h -= 5 """

        h += k_in_row(state.board, (x,y), player, (0,1) )
        h += k_in_row(state.board, (x,y), player, (1,0) )
        h += k_in_row(state.board, (x,y), player, (1,1) )
        h += k_in_row(state.board, (x,y), player, (1,-1) )

        h -= k_in_row(state.board, (x,y), enemy, (0,1) )
        h -= k_in_row(state.board, (x,y), enemy, (0,1) )
        h -= k_in_row(state.board, (x,y), enemy, (0,1) )
        h -= k_in_row(state.board, (x,y), enemy, (0,1) )

    return h


def legal_moves(state):
    return [(x, y) for (x, y) in state.moves
            if y == 1 or (x, y - 1) in state.board]

def plenemy(player):
    if player == 'X':
        return 'O'
    else:
        return 'X'


def k_in_row(board, (m,n), player, (delta_x, delta_y) ):
    enemy = plenemy(player)
    x, y = m, n
    n = 0
    k = 0
    while (board.get((x, y)) != enemy )  and x < 8 and y < 7  :
        if(board.get((x, y)) == player):
            n += 4
            k += 1
        else:
            n+=2
        x, y = x + delta_x, y + delta_y
    x, y = m, n
    while (board.get((x, y)) != enemy )  and x > 0 and y > 0 :
        if (board.get((x, y)) == player):
            n += 4
            k += 1
        else:
            n += 2
        x, y = x - delta_x, y - delta_y
    n -= 4
    k -= 1
    if k == 4:
        return n + 1000
    else: 
        return n



