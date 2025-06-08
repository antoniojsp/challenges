# https://leetcode.com/problems/number-of-provinces/description/
from collections import defaultdict

class Solution:
    def create_adj_list(self, matrix :list[list[int]]) -> Dict[int, list[int]]:
        adj_list = defaultdict(list)
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 1:
                    adj_list[i].append(j)
        return adj_list

    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        adj_list = self.create_adj_list(isConnected) # represetation of all the connection between cities
        new_cities_visited = set() # to keep track new provinces
        city = len(isConnected)
        provinces = 0
        for i in range(city):
            if i not in new_cities_visited: # since the matrix always include the connection to the city itself, then we can make sure is marked as visited.
                provinces+=1
                S = [i]
                while S:
                    node = S.pop()
                    new_cities_visited.add(node)
                    for connection in adj_list[node]:
                        if connection not in new_cities_visited:
                            S.append(connection)

        return provinces
