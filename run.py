import games
import heuristic

game = games.ConnectFour()
state = game.initial

dificulty = 0
deep = 4
while (dificulty == 0):
    dif = raw_input("Select dificulty: 1 (Facil), 2 (Medium), 3 (Dificil): ")
    dificulty = int(str(dif).strip())
    if (dificulty == 1):
        h = heuristic.h0
    elif (dificulty == 2):
        h = heuristic.h1
    elif (dificulty == 3):
        h = heuristic.h2
        deep = raw_input("Select depth : 2 or 4 :")
        depth = int(str(deep).strip())
        if deep == 2 : deep = 2
        else: deep =4

    else :
        print "Dificulty not valid ,please try again ..."
        dificulty = 0




primo = raw_input("Who start first: 1 (Machine  or 2 (Person) : ")
first = int(str(primo).strip())

if(first == 1):
    player = 'X'
elif(first == 2):
    player = 'O'
else:
    print("Input not legal! Machine start first! ")
    player = 'X'


while True:
    print "Jugador a mover:", game.to_move(state)
    game.display(state)

    if player == 'O':
        col_str = raw_input("Movimiento: ")
        coor = int(str(col_str).strip())
        x = coor
        y = -1
        legal_moves = game.legal_moves(state)
        for lm in legal_moves:
            if lm[0] == x:
                y = lm[1]

        state = game.make_move((x, y), state)
        player = 'X'
    else:
        print "Thinking..."
        #move = games.minimax_decision(state, game)
        #move = games.alphabeta_full_search(state, game)


        move = games.alphabeta_search(state, game, d = deep, eval_fn = h)

        state = game.make_move(move, state)
        player = 'O'
    print "-------------------"
    if game.terminal_test(state):
        game.display(state)
        print "Final de la partida"
        break
