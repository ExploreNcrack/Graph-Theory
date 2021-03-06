from AdjMatrix import Graph

if __name__ == '__main__':
	print("Undirected Graph")
	G =Graph(6, directed=False)
	G.set_vertex(0,'a')
	G.set_vertex(1,'b')
	G.set_vertex(2,'c')
	G.set_vertex(3,'d')
	G.set_vertex(4,'e')
	G.set_vertex(5,'f')
	G.set_edge('a','e',10)
	G.set_edge('a','c',20)
	G.set_edge('c','b',30)
	G.set_edge('b','e',40)
	G.set_edge('e','d',50)
	G.set_edge('f','e',60)
	print("Vertices of Graph")
	print(G.get_vertex())
	print("Edges of Graph")
	print(G.get_edges())
	print("Adjacency Matrix of Graph")
	print(G.get_matrix())
	print("------------------------------------------------------")
	print("Directed Graph")
	G =Graph(6,directed=True)
	G.set_vertex(0,'a')
	G.set_vertex(1,'b')
	G.set_vertex(2,'c')
	G.set_vertex(3,'d')
	G.set_vertex(4,'e')
	G.set_vertex(5,'f')
	G.set_edge('a','e',10)
	G.set_edge('a','c',20)
	G.set_edge('c','b',30)
	G.set_edge('b','e',40)
	G.set_edge('e','d',50)
	G.set_edge('f','e',60)
	print("Vertices of Graph")
	print(G.get_vertex())
	print("Edges of Graph")
	print(G.get_edges())
	print("Adjacency Matrix of Graph")
	print(G.get_matrix())