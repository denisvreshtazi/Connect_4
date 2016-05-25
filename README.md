# Connect_4
FSI Project 1

Trabajo 1 - Búsqueda con adversario(Conecta 4) Denis Vreshtazi

The game is Connect 4 base on Minimax search and AlphaBeta Pruning. 
The file run.py is changed in order to let the player choose who is going to start first (player or machine). The first who starts has the mark: ‘X’ and the second : ‘O’ . The player can also choose between three difficulty level :  1, 2 or 3. Every difficulty level is corresponding to one Heuristic which is implemented at the file heuristic.py.  In the third difficulty level the player can choose between two different deep level: 2 and 4, making the game harder.
A new file is created heuristic.py, in which are implemented the 3 different heuristics. The first one “h0”, is based on an aleatory way of deciding the moves, making and the game more easy. 
The second one “h1”, first verifies is any of the players have won by checking its state, and than decide to play in an aleatory way.
The third heuristic “h2”,  verifies  if any of the players  has won than continue the game by the moves decided in the legal_moves() function. This heuristic uses the k_in_row function to count my occupied position in all 4 the directions. The k_in_row function add 4 if it finds myplay, 2 if it finds an empty space, and if the plays are 4 in a row it add 1000. 
The same is also done for the opponent, with the only difference that its value is removed from the player heuristic. 
The games.py is also changed in order to accept player as an input of eval_fn and minvalue , so they can be compatible with the heuristic functions. 


