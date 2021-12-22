#include <iostream>
#include<bits/stdc++.h>
using namespace std;
# define INF 0x3f3f3f3f
  
// iPair ==>  Integer Pair
typedef pair<long long, long long> iPair;
  
// This class represents a directed graph using
// adjacency list representation
class Graph
{
    long long V;    // No. of vertices
  
    // In a weighted graph, we need to store vertex
    // and weight pair for every edge
    list< pair<long long, long long> > *adj;
  
public:
    Graph(long long V);  // Constructor
  
    // function to add an edge to graph
    void addEdge(long long u, long long v, long long w);
  
    // print longs shortest path from s
    void shortestPath(long long s);
};
  
// Allocates memory for adjacency list
Graph::Graph(long long V)
{
    this->V = V;
    adj = new list<iPair> [V];
}
  
void Graph::addEdge(long long u, long long v, long long w)
{
    adj[u].push_back(make_pair(v, w));
    //adj[v].push_back(make_pair(u, w));
}
  
// Prlong longs shortest paths from src to all other vertices
void Graph::shortestPath(long long src)
{
    // Create a priority queue to store vertices that
    // are being preprocessed. This is weird syntax in C++.
    // Refer below link for details of this syntax
    // https://www.geeksforgeeks.org/implement-min-heap-using-stl/
    priority_queue< iPair, vector <iPair> , greater<iPair> > pq;
  
    // Create a vector for distances and initialize all
    // distances as infinite (INF)
    vector<long long> dist(V, INF);
  
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
        long long u = pq.top().second;
        pq.pop();
  
        // 'i' is used to get all adjacent vertices of a vertex
        list< pair<long long, long long> >::iterator i;
        for (i = adj[u].begin(); i != adj[u].end(); ++i)
        {
            // Get vertex label and weight of current adjacent
            // of u.
            long long v = (*i).first;
            long long weight = (*i).second;
  
            //  If there is shorted path to v through u.
            if (dist[v] > dist[u] + weight)
            {
                // Updating distance of v
                dist[v] = dist[u] + weight;
                pq.push(make_pair(dist[v], v));
            }
        }
    }
  
    // Prlong long shortest distances stored in dist[]
    printf("Vertex   Distance from Source\n");
    for (long long i = 0; i < V; ++i)
        printf("%lld \t\t %lld\n", i, dist[i]);
}

using namespace std;
int main(){
    long long n=100;
    long long N=5*n;
    vector<vector<long long> > v;
    for (long long i=0;i<n;i++){
        string l;
        cin>>l;
        vector<long long> vv;
        v.push_back(vv);
        for (long long j=0;j<n;j++){
            v[i].push_back(l[j]-'0');
        }
    }
    long long V = N*N;
    Graph g(V);
  
    //  making above shown graph
    for (long long i=0;i<n;i++){
        for (long long j=0;j<n;j++){
            for (long long ti=0;ti<5;ti++){
            for (long long tj=0;tj<5;tj++){
                if (i+ti*n<N-1)
                    g.addEdge((i+ti*n+1)*N+(j+tj*n),((i+ti*n)+0)*N+(j+tj*n), (v[i][j]+ti+tj-1)%9 +1);
                if ((j+tj*n)<N-1)
                    g.addEdge((i+ti*n)*N+(j+tj*n)+1,(i+ti*n)*N+(j+tj*n)+0, (v[i][j]+ti+tj-1)%9 +1);
                if ((i+ti*n)>0)
                    g.addEdge(((i+ti*n)-1)*N+(j+tj*n),((i+ti*n)-0)*N+(j+tj*n), (v[i][j]+ti+tj-1)%9 +1);
                if ((j+tj*n)>0)
                    g.addEdge((i+ti*n)*N+(j+tj*n)-1,(i+ti*n)*N+(j+tj*n)-0, (v[i][j]+ti+tj-1)%9 +1);
            }}
            
        }
    }
    
    g.shortestPath(0);
  
    return 0;
}