
// https://leetcode.com/problems/flood-fill/description/


function floodFill(image: number[][], sr: number, sc: number, color: number): number[][] {
    const directions = [[0,-1], [0,1], [1,0], [-1,0]]
    const stack = [[sr, sc]];
    const original = image[sr][sc];
    if(original === color){
        return image;
    }
    image[sr][sc] = color;
    while(0 < stack.length){
        const node = stack.pop();
        if(!node){
            continue;
        }
        const [row, col] = node;
        for(const [i, j] of directions){
            const next_row = row + i;
            const next_col = col + j;
            if ( 0 <= next_row &&
                next_row < image.length &&
                0 <= next_col &&
                next_col < image[0].length &&
                image[next_row][next_col] === original){
                    image[next_row][next_col] = color;
                    stack.push([next_row, next_col])
            }
        }
    }
    return image;
};