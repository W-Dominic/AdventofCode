def isVisible(i, j, matrix):
    num_rows = len(matrix)
    num_cols = len(matrix[0])

    val = matrix[i][j]
    b_left = True
    b_right = True
    b_up = True
    b_down = True
    #left
    for c in range(0,j):
        if matrix[i][c] >= val:
            b_left = False
            break
    #right
    for c in range(j+1,num_cols):
        if matrix[i][c] >= val:
            b_right = False
            break
    #up
    for r in range(0,i):
        if matrix[r][j] >= val:
            b_up = False
            break
    #down
    for r in range(i+1,num_rows):
        if matrix[r][j] >= val:
            b_down = False
            break
    return b_left or b_right or b_up or b_down

if __name__ == "__main__":
    f = open("input.txt").read().splitlines()
    data = []
    for i in f:  
        data.append(i)

    matrix = []
    for r in data:
        matrix.append(r)

    num_rows = len(matrix)
    num_cols = len(matrix[0])

    num_visible = num_cols*2 + num_rows*2 - 4

    for i in range(1,num_rows-1):
        for j in range(1,num_cols-1):
            if isVisible(i, j, matrix):
                num_visible += 1
                print(i,j)



    print(num_visible)