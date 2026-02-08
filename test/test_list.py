def test_list(matrix: list[list[int]]) -> list[list[int]] :
	trixma = list()
	for ligne in range(matrix.__len__()) :
		trixma.append(list(matrix[ligne]))
		trixma[ligne].reverse()
	print("matrix", matrix)
	print("trixma", trixma)
	return (trixma)

print(test_list([[45, 69], [85, 24], [965, 147], [2, 9]]))
#print(test_list([45, 69, 85, 24, 965, 147, 2, 9]))
