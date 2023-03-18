#include <iostream>
#include <vector>
#include <set>
#include <unordered_map>

using namespace std;

vector <int> dfs(vector<vector<int>> &graph, unordered_map<int, int>& visited, int node, bool &flag)
{
    vector <int> ans;
    visited[node] = 1;
    for (auto neigh: graph[node])
        if (visited.find(neigh) != visited.end())
        {
            if (visited[neigh] == 1) 
            {
                flag = false;
                return ans;
            }
        }
        else 
        {
            vector <int> res = dfs(graph, visited, neigh, flag);
            if (res.size() == 0)
                return res;
            ans.insert(ans.end(), res.begin(), res.end());
        }
    visited[node] = 2;
    ans.push_back(node);
    return ans;
}

int main()
{
    int v, e;
    cin >> v >> e;

    vector<vector<int>> graph;
    unordered_map <int, int> visited;
    for (int i = 0; i < v + 1; i++)
        graph.push_back(vector<int>());
    
    for (int i = 0; i < e; ++i)
    {
        int v1, v2;
        cin >> v1 >> v2;
        graph[v1].push_back(v2);
    }
    
    vector<int> ans;
    bool flag = true;
    for (int i = 1; i < v + 1; i++)
        if (visited.find(i) == visited.end())
        {
            vector<int> outp = dfs(graph, visited, i, flag);
            if (not flag)
            {
                cout << -1;
                break;
            }
            else ans.insert(ans.end(), outp.begin(), outp.end());
        }
        if (flag)
            for (auto it = ans.rbegin(); it != ans.rend(); it++)
                cout << *it << " ";
    return 0;
}
