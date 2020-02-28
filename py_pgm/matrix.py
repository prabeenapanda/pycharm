
R = int(input("Enter the number of rows:"))
C = int(input("Enter the number of columns:"))
matrix = []
for i in range(R):		 # A for loop for row entries
	a =[]
	for j in range(C):	 # A for loop for column entries
		a.append(int(input("Enter the entries row wise:")))
	matrix.append(a)
print(matrix) #[[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# For printing the matrix
for i in range(R):
	for j in range(C):
		print(matrix[i][j], end = " ")
	print()

mat = [[int(input("enter number:")) for x in range (C)] for y in range(R)]
print(mat) #[[1, 2], [3, 4]]
