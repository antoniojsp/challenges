//https://leetcode.com/problems/rotate-string/?envType=daily-question&envId=2026-05-03

function rotateString(s: string, goal: string): boolean {
    if (goal.length !== s.length){
        return false;
    }
    const double = s+s;
    // for(let i = 0; i < double.length; i++){
    //     if(double.slice(i, i+goal.length) === goal){
    //         return true;
    //     }
    // }
    return double.includes(goal);
};