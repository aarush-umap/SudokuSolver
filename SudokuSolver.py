import pprint

def solve(bo):
	arr = find_empty(bo)
	if len(arr) == 0:
		return True
	for i in range(1, 10):
		if is_valid(bo, i, arr[0], arr[1]):
			bo[arr[0]][arr[1]] = i
			if solve(bo):
				return True
			elif i == 9:
				bo[arr[0]][arr[1]] = 0
				return False
	bo[arr[0]][arr[1]] = 0
	return False

def is_valid(bo, num, row, col):
	#Checks row
	for b in range(len(bo[row])):
		if bo[row][b] == num and b != col:
			return False

	#Checks col
	for b in range(len(bo)):
		if bo[b][col] == num and b != row:
			return False

	#Checks square
	t_row = (row // 3) * 3
	t_col = (col // 3) * 3

	for r in range(t_row, t_row + 3):
		for c in range(t_col, t_col + 3):
			if num == bo[r][c] and (r != row and c != col):
				return False
	return True

def find_empty(bo):
	for r in range(len(bo)):
		for c in range((len(bo[0]))):
			if bo[r][c] == 0:
				return [r, c]
	return []

def print_board(bo):
	for row in range(len(bo)):
		if row % 3 == 0 and row != 0:
			print("- - - - - - - - - - - - - -")
		for col in range(len(bo[0])):
			if col % 3 == 0:
				print(" | ", end="")

			if col == 8:
				print(bo[row][col], end="\n")
			else:
				print(str(bo[row][col]) + " ", end="")


#board = [
#		[7, 8, 0, 4, 0, 0, 1, 2, 0],
#		[6, 0, 0, 0, 7, 5, 0, 0, 9],
#		[0, 0, 0, 6, 0, 1, 0, 7 ,8],
#		[0, 0, 7, 0, 4, 0, 2, 6, 0],
#		[0, 0, 1, 0, 5, 0, 9, 3, 0],
#		[9, 0, 4, 0, 6, 0, 0, 0, 5],
#		[0, 7, 0, 3, 0, 0, 0, 1, 2],
#		[1, 2, 0, 0, 0, 7, 4, 0, 0],
#		[0, 4, 9, 2, 0, 6, 0, 0, 7]
#	]

#board = [
#		[0,0,0,0,3,0,0,0,0],
#		[0,8,9,4,0,0,0,0,0],
#		[0,0,3,0,6,7,0,9,0],
#		[9,0,1,0,0,0,0,5,0],
#		[0,7,0,0,1,0,0,4,0],
#		[0,4,0,0,0,0,2,0,8],
#		[0,2,0,3,8,0,1,0,0],
#		[0,0,0,0,0,4,3,2,0],
#		[0,0,0,0,9,0,0,0,0]
#	]

board = [
		[9,0,0,0,0,0,5,0,0],
		[7,0,0,2,0,0,0,3,0],
		[2,0,5,7,4,0,0,0,0],
		[3,0,0,8,0,0,1,0,0],
		[0,0,0,5,0,1,0,0,0],
		[0,0,7,0,0,6,0,0,9],
		[0,0,0,0,1,5,9,0,2],
		[0,2,0,0,0,7,0,0,5],
		[0,0,9,0,0,0,0,0,3]
	]

pp = pprint.PrettyPrinter(width=41, compact = True)
print("\n\nBoard:\n\n")
print_board(board)
print("\n\nSolution:\n\n")
solve(board)
print_board(board)