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
<br/>The idea is to use the two indexes to represent two vertices and by accessing the value in the array with that index, we can know that whether or not there are edges between those vertices. In practice, the value in each cell(in the array), 0 or -1 represent there is no edge between the two vertices and if it is any value > 0, it represent the weight for that edge between those two vertices. In math, the value represent the number of edges between those two vertices.
<br/>Let the 2D array be adj[][], 
a slot **adj[i][j] = 1 indicates that there is an edge from vertex i to vertex j**.
### Property for Certain Graph
Adjacency matrix for **undirected graph** is always **symmetric**. Adjacency Matrix is also used to represent weighted graphs. If adj[i][j] = w, then there is an edge from vertex i to vertex j with weight w.

### Pros(Advantage) 
- This representation is easy to implement and follow
- The adjacency matrix is a good implementation for a graph **when the number of edges is large**
<br/> **Operations:**
  - **Removing** an edge takes **O(1)** constant time. 
  - **Queries** like whether there is an edge from vertex ‘u’ to vertex ‘v’ are efficient and can be done **O(1)** constant time.
### Cons(Disadvantage)
- Consumes more **space O(V<sup>2</sup>)**
- Even if the graph is **sparse**(*contains less number of edges, the matrix has lots of 0*) which is wasting lots of memory, it consumes the same space. (**A matrix is not a very efficient way to store sparse data.**)
- **Adding a vertex** is **O(V<sup>2</sup>) time**.
- Few real problems that approach full connectivity graph.
### Reference
https://www.geeksforgeeks.org/graph-and-its-representations/
https://interactivepython.org/courselib/static/pythonds/Graphs/AnAdjacencyMatrix.html
