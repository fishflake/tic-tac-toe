#tic-tac-toe game program by Rachel Ciavarella 2018 
#for Pair Programming task the Recurse Center Applicaiton

#Before your interview, write a program that lets two humans play a game of Tic Tac Toe in a terminal. 
#The program should let the players take turns to input their moves. 
#The program should report the outcome of the game.

#make an array that holds the board values
board = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

moveNumber = 0

verticalBar = " | "
horizontalBar = "-----------"

def drawBoard( ):
	#draw new board function
	print board[0] + verticalBar + board[1] + verticalBar + board[2] 
	print horizontalBar
	print board[3] + verticalBar + board[4] + verticalBar + board[5] 
	print horizontalBar
	print board[6] + verticalBar + board[7] + verticalBar + board[8] 
	return

drawBoard( )

print "Player X make your move, enter number 1 - 9 on the keyboard"



