#tic-tac-toe game program by Rachel Ciavarella 2018 
#for Pair Programming task the Recurse Center Application

#Before your interview, write a program that lets two humans play a game of Tic Tac Toe in a terminal. 
#The program should let the players take turns to input their moves. 
#The program should report the outcome of the game.
#-----------------------------------------------------------------------------------------------------

#set up game variables

#make an array that holds the board values
board = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

#Variable for a counter for the number of moves made
moveNumber = 0

#Variables for printing the board
verticalBar = " | "
horizontalBar = "-----------"
spacing = " "

#Bool for game over
gameOver = False

#-----------------------------------------------------------------------------------------------------

#Define Functions

#draw new board function
def drawBoard( ):
	print moveNumber
	print spacing 
	print board[0] + verticalBar + board[1] + verticalBar + board[2] 
	print horizontalBar
	print board[3] + verticalBar + board[4] + verticalBar + board[5] 
	print horizontalBar
	print board[6] + verticalBar + board[7] + verticalBar + board[8] 
	print spacing
	return

#A function to check if that space has already been used
def CheckSpace( space ):
	if board[space] == "X" or board[space] == "O":
		print "Try another spot buddy, this one's taken"
		return True


#A function to allow a move with a keyboard input
def play():
	move = input()
	global moveNumber

	if CheckSpace( move-1 ):
		return

	if moveNumber % 2 == 0:
	    board[move-1]= 'X' 
	else:
	    board[move-1]= 'O'
	moveNumber += 1



#A function to check if a player has won
def checkBoard( player ):

	if board[0] == player and board[1] == player and board[2] == player:
		return True

	elif board[3] == player and board[4] == player and board[5] == player:
		return True

	elif board[6] == player and board[7] == player and board[8] == player:
		return True

	elif board[0] == player and board[3] == player and board[6] == player:
		return True

	elif board[1] == player and board[4] == player and board[7] == player:
		return True

	elif board[2] == player and board[5] == player and board[8] == player:
		return True

	elif board[0] == player and board[4] == player and board[8] == player:
		return True

	elif board[2] == player and board[4] == player and board[6] == player:
		return True


#-----------------------------------------------------------------------------------------------------


#draw the board for the first time
drawBoard()

#Loop until 9 turns have been used
while gameOver == False and moveNumber < 9:
	#Alternate between X and O
	if moveNumber % 2 == 0:
	    print "Player X make your move, enter number 1 - 9 on the keyboard"
	else:
	    print "Player O make your move, enter number 1 - 9 on the keyboard"

	#Allow user to enter move
	play()
	drawBoard()

	global gameOver
	#Check if a player has won
	if checkBoard( "X" ): 
		print "PLAYER X WON!!"
		gameOver = True
	elif checkBoard( "O" ):
		print "PLAYER O WON!!"
		gameOver = True




















