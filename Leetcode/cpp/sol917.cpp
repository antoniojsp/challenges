
// https://leetcode.com/problems/reverse-only-letters/description/

class Solution {
public:

    bool is_alpha(char value){
        /*
        Checks if char is alpha (abc..z). Mostly for simplify syntax
        */
        return std::isalpha(static_cast<unsigned char>(value));
    }

    string reverseOnlyLetters(string s) {
        int start = 0;
        int end =  s.size()-1;

        while(start < end){
            bool l = is_alpha(s[start]);
            bool r = is_alpha(s[end]);
            if(!l){
                start++;
            }
            if(!r){
                end--;
            }
            if((l&&r) ){
                swap(s[start], s[end]);
                start++;
                end--;
            }
        }
        return s;
    }
};


class Solution {
public:
    vector<vector<int>> allPathsSourceTarget(vector<vector<int>>& graph) {
        int ending = graph.size()-1;
        pair<int, vector<int>> node(0, {0});

        vector<pair<int, vector<int>>> S;
        S.push_back(node);

        vector<vector<int>> result;

        while(!S.empty()){
            pair<int, vector<int>> temp = S.back();
            cout << temp.first;
            S.pop_back();
            if(ending == temp.first){
                result.push_back(temp.second);
            }

            for(auto i:graph[temp.first]){
                cout << i;
                temp.second.push_back(i);
                pair<int, vector<int>> nuevo = {i, temp.second};
                S.push_back(temp};
            }

        }

        return result;
    }
};


