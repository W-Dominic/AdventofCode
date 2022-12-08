def scenicScore(i, j, matrix):
    num_rows = len(matrix)
    num_cols = len(matrix[0])

    val = matrix[i][j]
    s_left = 1
    s_right = 1
    s_up = 1
    s_down = 1
    #left
    for c in range(j-1,0,-1):
        if matrix[i][c] >= val:
            break
        else:
            s_left += 1
    #right
    for c in range(j+1,num_cols-1):
        if matrix[i][c] >= val:
            break
        else:
            s_right += 1
    #up
    for r in range(i-1,0,-1):
        if matrix[r][j] >= val:
            break
        else:
            s_up += 1
    #down
    for r in range(i+1,num_rows-1):
        if matrix[r][j] >= val:
            break
        else:
            s_down += 1
    print(i,j, val, " || ", s_left, s_right, s_up, s_down)
    return s_left * s_right * s_up * s_down

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

    max_score = 0

    for i in range(1,num_rows-1):
        for j in range(1,num_cols-1):
            max_score = max(max_score, scenicScore(i,j,matrix))

    print(max_score)