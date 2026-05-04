
/**
 Do not return anything, modify matrix in-place instead.
 */
const transpose = (matrix:any) => {
    for(let i = 0; i < matrix.length; i++){
        for(let j = i; j < matrix[0].length; j++){
            [matrix[i][j], matrix[j][i]] = [matrix[j][i], matrix[i][j]]
        }
    }
}

const reverse = (matrix:any) => {
    for(let i = 0; i < matrix.length; i++){
        matrix[i].reverse()
    }
}

function rotate(matrix: number[][]): void {
    transpose(matrix)
    reverse(matrix)
};