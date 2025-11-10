/**
 * @param {number[][]} matrix
 * @return {void} Do not return anything, modify matrix in-place instead.
 */
var setZeroes = function(matrix) {
    
    let m = matrix.length  // no. of rows
    let n = matrix[0].length // no. of cols

    let rows = new Set() // set to store the rows where zero element is present
    let cols = new Set() // set to store the cols where zero element is present

    // finding the rows and cols that needs to be zeroed
    for (let i = 0; i < m; i++){
        for (let j = 0; j < n; j++){
            if (matrix[i][j] == 0){
                rows.add(i)
                cols.add(j)
            }
        }
    }

    // making the elements from the indices from rows and cols to zero
    for (let i = 0; i < m; i++){
        for (let j = 0; j < n; j++){
            if (rows.has(i) || cols.has(j)){
                matrix[i][j] = 0
            }
        }
    }
    
};