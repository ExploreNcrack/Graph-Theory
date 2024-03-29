<h1 align="center"><strong>Graph Theory</strong></h1>
Exploring graph theory in mathematical way</br>
<h2>Goal</h2>
Modeling problem as a graph is a very important technique in problem solving. Since we can nicely simplify the problem into basic components: nodes(or vertices) and edges, where a node in a graph can represent an object and an edge can represent some sort of relation between the objects. Further more, once we represent the problem as a graph, we can apply the mathematical graph theory(which has lots of nice properties about different kinds of graphs and so on.) to analyze the problem and possibly come up with an effective solution. 

<h2>Types of Graphs</h2>
<p>In general, by formal definition, a graph is <strong>an order triple</strong> <img src="G.jpg" align="center" border="0" alt="G=(V,E,\psi) " width="101" height="19" />, where <strong>V</strong> is a <strong>non-empty set of vertices(points)</strong>, <strong>E</strong> is a set of edges (lines) disjoint from V, and <img src="psi.jpg" align="center" border="0" alt="\psi" width="18" height="19" /> is a function that assigns to each edge, a pair of vertices (v,v’).</p>
<h3>Directed Graph</h3>
<p>A graph in which the edges are directed by arrows, indicating that the relationship, represented by the edge, only applies from one vertex to the other, but not the other way around. In other words, if a directed edge has an arrow from A to B, A is related to B, but B is not related to A.</p>
<p>In formal terms, a directed graph is an ordered pair G = (V, A) where
<ul>
  <li>V is a set whose elements are called vertices, nodes, or points;</li>
  <li>A is a set of ordered pairs of vertices, called arrows, directed edges (sometimes simply edges with the corresponding set named E instead of A), directed arcs, or directed lines.</li>
</ul>
</p>
<h3>Undirected Graph</h3>
<p>Undirected graph: A graph whose edges are not directed. Mary's graph is an undirected graph, because the routes between cities go both ways.</p>
<h3>Null Graph</h3>
<p>Also called an empty graph, a null graph is a graph in which there are no edges between any of its vertices.</p>
<h3>Simple Graph</h3>
<p>A graph in which there is at most one edge between each pair of vertices, and there are no <strong>loops</strong>, which is an edge from a vertex to itself.</p>
<h3>Complete Graph</h3>
<p>A simple undirected graph in which every pair of distinct vertices is connected by a unique edge.</p>
<h3>Complete Digraph</h3>
<p>A complete digraph is a directed graph in which every pair of distinct vertices is connected by a pair of unique edges (one in each direction).</p>

<h2>References</h2>
https://en.wikipedia.org/wiki/Directed_graph
https://www8.cs.umu.se/kurser/TDBA77/VT06/algorithms/BOOK/BOOK2/NODE72.HTM
https://medium.com/tebs-lab/modeling-problems-as-graphs-6ab451f03868
https://study.com/academy/lesson/graphs-in-discrete-math-definition-types-uses.html
