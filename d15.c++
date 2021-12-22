#include <iostream>
#include<bits/stdc++.h>
using namespace std;
# define INF 0x3f3f3f3f
  
// iPair ==>  Integer Pair
typedef pair<int, int> iPair;
  
// This class represents a directed graph using
// adjacency list representation
class Graph
{
    int V;    // No. of vertices
  
    // In a weighted graph, we need to store vertex
    // and weight pair for every edge
    list< pair<int, int> > *adj;
  
public:
    Graph(int V);  // Constructor
  
    // function to add an edge to graph
    void addEdge(int u, int v, int w);
  
    // prints shortest path from s
    void shortestPath(int s);
};
  
// Allocates memory for adjacency list
Graph::Graph(int V)
{
    this->V = V;
    adj = new list<iPair> [V];
}
  
void Graph::addEdge(int u, int v, int w)
{
    adj[u].push_back(make_pair(v, w));
    //adj[v].push_back(make_pair(u, w));
}
  
// Prints shortest paths from src to all other vertices
void Graph::shortestPath(int src)
{
    // Create a priority queue to store vertices that
    // are being preprocessed. This is weird syntax in C++.
    // Refer below link for details of this syntax
    // https://www.geeksforgeeks.org/implement-min-heap-using-stl/
    priority_queue< iPair, vector <iPair> , greater<iPair> > pq;
  
    // Create a vector for distances and initialize all
    // distances as infinite (INF)
    vector<int> dist(V, INF);
  
    // Insert source itself in priority queue and initialize
    // its distance as 0.
    pq.push(make_pair(0, src));
    dist[src] = 0;
  
    /* Looping till priority queue becomes empty (or all
      distances are not finalized) */
    while (!pq.empty())
    {
        // The first vertex in pair is the minimum distance
        // vertex, extract it from priority queue.
        // vertex label is stored in second of pair (it
        // has to be done this way to keep the vertices
        // sorted distance (distance must be first item
        // in pair)
        int u = pq.top().second;
        pq.pop();
  
        // 'i' is used to get all adjacent vertices of a vertex
        list< pair<int, int> >::iterator i;
        for (i = adj[u].begin(); i != adj[u].end(); ++i)
        {
            // Get vertex label and weight of current adjacent
            // of u.
            int v = (*i).first;
            int weight = (*i).second;
  
            //  If there is shorted path to v through u.
            if (dist[v] > dist[u] + weight)
            {
                // Updating distance of v
                dist[v] = dist[u] + weight;
                pq.push(make_pair(dist[v], v));
            }
        }
    }
  
    // Print shortest distances stored in dist[]
    printf("Vertex   Distance from Source\n");
    for (int i = 0; i < V; ++i)
        printf("%d \t\t %d\n", i, dist[i]);
}

using namespace std;
int main(){
    int n=10;
    int N=6*n;
    vector<vector<int> > v;
    for (int i=0;i<n;i++){
        string l;
        cin>>l;
        vector<int> vv;
        v.push_back(vv);
        for (int j=0;j<n;j++){
            v[i].push_back(l[j]-'0');
        }
    }
    int V = N*N;
    Graph g(V);
  
    //  making above shown graph
    for (int i=0;i<n;i++){
        for (int j=0;j<n;j++){
            for (int ti=0;ti<6;ti++){
            for (int tj=0;tj<6;tj++){
                if (i+ti*6<N-1)
                    g.addEdge((i+ti*6)*N+(j+tj*6),((i+ti*6)+1)*N+(j+tj*6), (v[(i+1)%n][j]+ti+tj-1)%9 +1);
                if ((j+tj*6)<N-1)
                    g.addEdge((i+ti*6)*N+(j+tj*6),(i+ti*6)*N+(j+tj*6)+1, (v[i][(j+1)%n]+ti+tj-1)%9 +1);
                if ((i+ti*6)>0)
                    g.addEdge((i+ti*6)*N+(j+tj*6),((i+ti*6)-1)*N+(j+tj*6), (v[(i-1+n)%n][j]+ti+tj-1)%9 +1);
                if ((j+tj*6)>0)
                    g.addEdge((i+ti*6)*N+(j+tj*6),(i+ti*6)*N+(j+tj*6)-1, (v[i][(j-1+n)%n]+ti+tj-1)%9 +1);
            }}
            
        }
    }
    
    g.shortestPath(0);
  
    return 0;
}