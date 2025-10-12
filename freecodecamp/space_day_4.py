


def find_landing_spot(matrix):
    minimum = float('inf')
    result = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            temp = 0
            if matrix[i][j] == 0:
                #up
                if 0 < i:
                    temp+=matrix[i-1][j]
                #down
                if i < len(matrix)-1:
                    temp+=matrix[i+1][j]
                #left
                if 0 < j:
                    temp+=matrix[i][j-1]
                #right
                if j < len(matrix[0])-1:
                    temp+=matrix[i][j+1]
                if minimum > temp:
                    result = [i, j]
                    minimum = temp
    return result

print(find_landing_spot([[1, 0], [2, 0]]))