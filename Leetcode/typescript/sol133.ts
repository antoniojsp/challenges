
//https://leetcode.com/problems/clone-graph/description/

/**
 * Definition for _Node.
 * class _Node {
 *     val: number
 *     neighbors: _Node[]
 *
 *     constructor(val?: number, neighbors?: _Node[]) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.neighbors = (neighbors===undefined ? [] : neighbors)
 *     }
 * }
 *
 */


function cloneGraph(node: _Node | null): _Node | null {
    if(!node){
        return node;
    }
	const Q:_Node[] = [node];
    const mapa:Map<_Node, _Node> = new Map();
    // mapa < node original, node copy >
    mapa.set(node, new _Node(node.val));
    while(Q.length > 0){
        const curr:_Node | undefined = Q.shift();
        for(const i of curr.neighbors){
            if(!mapa.has(i)){
                mapa.set(i, new _Node(i.val));
                Q.push(i);
            }
            mapa.get(curr).neighbors.push(mapa.get(i))
        }
    }
    return mapa.get(node);
};