# Christina Smithers
# Interview puzzle - Sudoku solver
# Please note that I borrowed code and adapted it 
#There are other examples out there that are better, but this was simple and quick


import sys

#setup for empty numbers
#setup for the row for non-filled
def same_row (i,j):
	#return that row with 9 cells
	return (i/9 == j/9)
#do the same for column
def same_column(i, j):
	#9 columns but cannot have dupes
	return (i - j) % 9 == 0
#make sure the same cell isn't used again
def same_cell (i, j):
	#27 for 3 grids of sudoku per column and row
	return (i/27 == j/27 and i % 9 / 3 == j % 9 / 3) #also then divide into 3 blocks

#move through the grid
def r(a):
	#0 is treated as a blank
	i = a.find('0')
	#looks for bad entries and exits if so
	if i == -1:
		sys.exit(a)

def dupes(a):
	#check for numbers already in teh same row, column, or cell as "i"
	used_numbers = set()
	#using a for loop since going through a list regardless of a condition through all 81 sudoku cells
	for j in range(81):
	#looking for the numbers until done on row, column, and cell
		if same_row (i, j) or same_column (i, j) or same_cell (i, j):
		used_numbers.add(a[j])

#check to see if n is not one of the used numbers
	for guess in '123456789':
		if guess not in empty_numbers:
			#looks before and after so you read left to right and top to bottom
			#cocatenates all fields UP TO position i is in, the guess (n), and then AFTER  position i
			#filler is a function that finds an unfilled cell then fills it with a number, calls itself 
			#until there are no more numbers then exits
			filler(a[:i] + guess a [i + 1:])

if __name__ == '__main__':
	#checks to make sure everything is done within the limits
	if len(sys.argv) == 2 and len(sys.argv[1]) ==81:
		filler(sys.argv[1])

	else:
		print 'Python Sudoku Puzzle'
		print 'Where the puzzle is 81 characters of string read R->L and Top->Bottom.  0 represents an empty cell'





