import math

board = [" " for _ in range(9)]

def print_board():
	for i in range(3):
		print(f"{board[3*i]} | {board[3*i+1]} | {board[3*i+2]}")
		if i < 2:
			print("----------")

def is_winner(b, player):
	win_combinations = [
		[0, 1, 2], [3, 4, 5], [6, 7, 8],
		[0, 3, 6], [1, 4, 7], [2, 5, 8],
		[0, 4, 8], [2, 4, 6]
	]

	return any(all(b[pos]==player for pos in combo) for combo in win_combinations)

def is_draw(b):
	return ' ' not in b

def get_available_moves(b):
	return [i for i in range(9) if b[i]==" "]

def minimax(b, depth, is_maximizing):
	if is_winner(b, 'O'):
		return 1
	if is_winner(b, 'X'):
		return -1
	if is_maximizing:
		best_score = -math.inf
		for move in get_available_moves(b):
			b[move] = 'O'
			score = minimax(b, depth+1, False)
			b[move] = " "
			best_score = max(score, best_score)
		return best_score
	else:
		best_score = math.inf
		for move in get_available_moves(b):
			b[move] = 'X'
			score = minimax(b, depth+1, True)
			b[move] = " "
			best_score = min(score, best_score)
		return best_score

def best_move():
	move = -1
	best_score = -math.inf
	for i in get_available_moves(board):
		board[i] = 'O'	
		score = minimax(board, 0, False)
		board[i] = " "
		if score > best_score:
			best_score = score
			move=i
	return move

board[0] = 'X'
board[4] = 'O'
board[1] = 'X'

print("Board before AI move: ")
print_board()

ai_choice = best_move()
board[ai_choice] = 'O'
print("\nBoard after AI move: ")
print_board()
