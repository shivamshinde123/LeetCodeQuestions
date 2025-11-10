/**
 * @param {number[][]} matrix
 * @return {void} Do not return anything, modify matrix in-place instead.
 */
var rotate = function(matrix) {
    
    m = matrix.length

    for (let i = 0; i < m; i++){
        for (let j = 0; j < i; j++){
            let element = matrix[i][j]
            matrix[i][j] = matrix[j][i]
            matrix[j][i] = element
        }
    }

    for (let i = 0; i < m; i++){
        matrix[i].reverse()
    }
};