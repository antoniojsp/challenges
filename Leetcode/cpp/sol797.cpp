class Solution {
public:
    vector<vector<int>> allPathsSourceTarget(vector<vector<int>>& graph) {
        int ending = graph.size()-1; // find the ending node
        vector<pair<int, vector<int>>> S; // vector holding the pairs (current node, path so far)
        S.push_back({0, {0}});

        vector<vector<int>> result;

        while(!S.empty()){ // using
            auto temp = S.back(); // gets pair (int, path)
            S.pop_back();
            if(ending == temp.first){ // if ending found, add path and skip a loop (no need to look for the end node's children)
                result.push_back(temp.second);
                continue;
            }

            for(auto i:graph[temp.first]){ // add each children from the current node to the stack
                auto new_node = temp.second;
                new_node.push_back(i);
                S.push_back({i, new_node});
            }
        }

        return result;
    }
};