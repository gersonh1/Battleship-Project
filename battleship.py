#Coder: Gerson Hernandez, Yafet Kassa
import random
# print a player's board to the console
def print_board(l):
	print("  1 2 3 4 5 ")
	for row in range(0, len(l)):
		print(str(row+1) + ' ' + ' '.join(l[row]))

# we're gonna be using this a bunch
def rand():
	return random.randint(0, 4)
# set up the game board and the player/opponent boards and guesses
def init():

	# board is initially empty for both players
	p1_board = [ ['-' for i in range(0, 5)] for j in range(0, 5) ]
	p2_board = [ ['-' for i in range(0, 5)] for j in range(0, 5) ]


	# populate the game boards with boats
	for board in [p1_board, p2_board]:
		for x in range(0, 5):
			i = rand()
			j = rand()
			# if there's already a boat at this position, generate more random
			# numbers and check again
			while board[i][j] == 'b':
				i = rand()
				j = rand()
			board[i][j] = 'b'

	# guesses are initially empty
	p1_guesses = [ ['-' for i in range(0, 5)] for j in range(0, 5) ]
	p2_guesses = [ ['-' for i in range(0, 5)] for j in range(0, 5) ]

	return (p1_board, p1_guesses, p2_board, p2_guesses)


def validate_input_guess():
	x, y = -1, -1
	while not 1 <= x <= 5 or not 1 <= y <= 5:
		guess = input("Please enter coordinates you haven't shot at yet. Example: 2 3\n")
		try:
			x, y = int(guess.split()[0]), int(guess.split()[1])
		except:
			print("Please enter integers 1-5 separated by a space.")
	return x, y

# creating the game
p1_board, p1_guesses, p2_board, p2_guesses = init()

# store the boards and guesses so we can get a player's boards by a single index
boards = [p1_board, p2_board]
guesses = [p1_guesses, p2_guesses]
lives = [5, 5]

# this represents the player turns. 1 = player 1, 2 = player 2
# the turns switch initially 
player_turn = 2



# game goes until a condition breaks it out
while True:
	
	# switch turns
	if player_turn == 1: 
		player_turn = 2
		enemy_board = boards[0]
		enemy_life_index = 0
		guess = guesses[1]

	else:
		player_turn = 1
		enemy_board = boards[1]
		enemy_life_index = 1
		guess = guesses[0]


	print(f"Player {player_turn}'s turn! _____________________________")
	print("These are your guesses currently:")
	print_board(guess)
	print()
	x, y = validate_input_guess()

	# if we've already made that guess, get input again
	while guess[y-1][x-1] != '-':
		x, y = validate_input_guess()

	# a hit!
	if enemy_board[y-1][x-1] == 'b':

		enemy_board[y-1][x-1] = '*'
		guess[y-1][x-1] = '*'

		#check to see whether that was their last life or not
		if lives[enemy_life_index] == 1:
			print(f"~~~Player {player_turn} wins~~~ \n Loser's board: ")
			print_board(enemy_board)
			break

		print(f"*** It's a hit! ***{lives[enemy_life_index]}")

		lives[enemy_life_index] -= 1

	else: # a miss
		guess[y-1][x-1] = 'o'
		print(f"Player {player_turn} misses!")

	print('\n' * 5)
