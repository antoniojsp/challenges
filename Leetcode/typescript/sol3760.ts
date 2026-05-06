


function maxDistinct(s: string): number {
    let sets = new Set<string>();
    for(const i of s){
        sets.add(i);
    }
     return sets.size
};