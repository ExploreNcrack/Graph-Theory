class Graph:
	def __init__(self, numVertex, directed=False):
		"""
		Init all necessary attributes for the data structure
		"""
		# indicate whether or not this is a directed or undirected graph
		self.directed = directed 
		# init the main 2-D array for storing graph
		self.adjMatrix = []
		# array size will be n x n (square matrix)
		for i in range(numVertex):
			new = []
			for j in range(numVertex):
				# content can be either number of edges between two vertices or the cost of the edge between the two vertices
				new.append(0)  # the content will represent number of edges between vertex i and vertext j
			self.adjMatrix.append(new)
		# total number of vertex
		self.numVertex = numVertex
		# map vertex label id to the actual vertex number
		# key   as label id
		# value as vertex number 
		self.vertices = {}
		# index   as the vertex number 
		# content as the label id 
		self.verticeslist = [0]*numVertex

	def set_vertex(self, vertex, labelID):
		assert (0 <= vertex <= self.numVertex), "The vertex number is exceeding the number of vertices in the graph."
		self.vertices[labelID] = vertex
		self.verticeslist[vertex] = labelID

	def set_edge(self, frm, to, numEdge):
		frm = self.vertices[frm]	
		to = self.vertices[to]
		if not self.directed:
			# undirected graph
			self.adjMatrix[frm][to] = numEdge 
			self.adjMatrix[to][frm] = numEdge
		else:
			# directed graph
			self.adjMatrix[frm][to] = numEdge

	def get_vertex(self):
		return self.verticeslist

	def get_edges(self):
		edges = []
		if not self.directed:
			vertexPair = {}
			for i in range(self.numVertex):
				for j in range(self.numVertex):
					if self.adjMatrix[i][j] != 0 and vertexPair.get(str(i)+str(j))==None and vertexPair.get(str(j)+str(i))==None:
						edges.append([self.verticeslist[i], self.verticeslist[j], self.adjMatrix[i][j]])
						vertexPair[str(i)+str(j)] = 0
		else:
			for i in range(self.numVertex):
				for j in range(self.numVertex):
					if self.adjMatrix[i][j] != 0:
						edges.append([self.verticeslist[i], self.verticeslist[j], self.adjMatrix[i][j]])
		return edges

	def get_matrix(self):
		return self.adjMatrix

	def get_num_edge(self, frm, to):
		frm = self.vertices[frm]	
		to = self.vertices[to]
		return self.adjMatrix[frm][to]

	def check_edge(self, frm, to):
		frm = self.vertices[frm]	
		to = self.vertices[to]
		return self.adjMatrix[frm][to] != 0
