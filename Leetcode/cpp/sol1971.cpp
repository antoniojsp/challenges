
// https://leetcode.com/problems/find-if-path-exists-in-graph/

class Solution {
public:
    void print(unordered_map<int, vector<int>>& map_list ){
        /*for testing*/
        for(auto key_val:map_list){
            cout << key_val.first << ":";
            for(auto i:key_val.second){
                cout << i <<" ";
            }
            cout << endl;
        }
    }

    unordered_map<int, vector<int>> create_adj_list(int n, vector<vector<int>>& edges){
        unordered_map<int, vector<int>>  adj_list;
        for(auto const& pair:edges){
            adj_list[pair[0]].push_back(pair[1]);
            adj_list[pair[1]].push_back(pair[0]);
        }
        return adj_list;
    }

    bool validPath(int n, vector<vector<int>>& edges, int source, int destination) {
        unordered_map<int, vector<int>> mapa = create_adj_list(n, edges);
        vector<int> S = {source};
        set<int> seen = {source};
        while(!S.empty()){
            int current = S.back();
            S.pop_back();
            if (current == destination){
                return true;
            }
            for(auto i:mapa[current]){
                if(!seen.count(i)){
                    S.push_back(i);
                    seen.insert(i);
                }
            }
        }
        return false;
    }
};