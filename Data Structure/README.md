# Data Strcture for Storing Graph information
Exploring different type of data structure representation of a graph in terms of complexity of different operations.
## Most commonly used representations of a graph.
- Adjacency Matrix
- Adjacency List
## Adjacency Matrix
### Definition
An adjacency matrix is a square matrix used to represent a finite graph. The elements of the matrix indicate whether pairs of vertices are adjacent or not in the graph.
</br>
For a graph G with vertices [v<sub>1</sub>, v<sub>2</sub>, .., v<sub>n</sub>], the adjacency matrix of G is the **n x n matrix**(_square matrix_)
**A=(a<sub>ij</sub>)** such that **a<sub>ij</sub>** is the number of edges between v<sub>i</sub> and v<sub>j</sub>.
<br/>
Note: loop count once each.
<br/>**a<sub>ij</sub>**, when i=j, is the number of loops for that vertex.
### Representation
Adjacency Matrix can be represented by a **2D array** of size V x V where V is the number of vertices in a graph. 
<br/>Let the 2D array be adj[][], 
a slot **adj[i][j] = 1 indicates that there is an edge from vertex i to vertex j**.
### Property for Certain Graph
Adjacency matrix for **undirected graph** is always **symmetric**. Adjacency Matrix is also used to represent weighted graphs. If adj[i][j] = w, then there is an edge from vertex i to vertex j with weight w.
