#include <iostream>
#include <vector>
#include <set>

using namespace std;

vector <int> dfs(vector<vector<int>> &graph, set<int>& visited, int node)
{
    vector <int> ans;
    ans.push_back(node);
    visited.insert(node);
    for (auto neigh: graph[node])
        if (visited.find(neigh) == visited.end())
        {
            vector <int> res = dfs(graph, visited, neigh);
            ans.insert(ans.end(), res.begin(), res.end());
        }
    return ans;
}

int main()
{
    int v, e;
    cin >> v >> e;

    vector<vector<int>> graph;
    set <int> visited;
    for (int i = 0; i < v + 1; i++)
        graph.push_back(vector<int>());
    
    for (int i = 0; i < e; ++i)
    {
        int v1, v2;
        cin >> v1 >> v2;
        graph[v1].push_back(v2);
        graph[v2].push_back(v1);
    }
    
    int n_comp = 0;
    vector<vector<int>> comp;
    for (int i = 1; i < v + 1; i++)
        if (visited.find(i) == visited.end())
        {
            comp.push_back(dfs(graph, visited, i));
            n_comp++;
        }
    cout << n_comp << endl;
    for (auto c: comp)
    {
        cout << c.size() << endl;
        for (auto x: c)
            cout << x << " ";
        cout << endl;
    }
    return 0;
}
