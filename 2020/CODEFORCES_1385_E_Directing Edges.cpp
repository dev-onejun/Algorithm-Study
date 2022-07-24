/*
    * Quest URL : https://codeforces.com/problemset/problem/1385/E
    * Aaaaiiiiiee

    * First Commit  : 2020-07-18
    * Last Commit   : 2020-07-18
*/
#include <iostream>
#include <vector>
#include <stack>
using namespace std;

// n : the number of vertices. m : the number of edges.
int n, m;
// graph : <t, <x, y>>
vector<pair<int, pair<int, int>>> graph;
// directed_graphs : Make Data_set into directed graphs
vector<vector<int>> directed_graphs;

vector<int> MakeDirectedGraph(int i)
{
    vector<int> directed_graph(n);
    for(; i<graph.size(); i++)
    {
        int cur_t = graph[i].first;
        int cur_x = graph[i].second.first, cur_y = graph[i].second.second;

        if(cur_t == 1)      // if the edge is directed
            directed_graph[cur_x] = cur_y;
        else if(cur_t == 0) // if the edge is undirected
        {
            directed_graph[cur_y] = cur_x;
            graph[i].first = 1;
            directed_graphs.push_back(MakeDirectedGraph(i));
            graph[i].first = 0;
        }
    }
    directed_gra

    return directed_graphs;
}

void dfs(vector<vector<int>>& directed_graphs)
{
    stack<int> s;
    for(int start= 1; start <= n; start++)
    {
        s.push(start);
        while(!s.empty())
        {
            int x = s.top();    s.pop();
        
        }
    }
}

int main(void)
{
    int t;  cin >> t;   // input the number of test cases.
    while(t--)
    {
        cin >> n >> m;
        for(int i=0; i<m; i++)
        {
            int t, x, y;    cin >> t >> x >> y;
            graph.push_back(make_pair(t, make_pair(x, y)));
        }
        directed_graphs.push_back(MakeDirectedGraph(0));
        dfs(directed_graphs);

        graph.clear();
    }
    return 0;
}
