class Graph:
    """
    Class Graph
    Arguments: none
    Instantiate: Graph()
    :return: nothing
    """
    def __init__(self):
        self.adjacency_list = {}
        # key: value pair
        # length
        # easily access the keys or the values with a simple loop

        # Time Complexity:  0(1)

    def add_vertex(self, value):
        """
        Method: add vertex
        Arguments: value
        Add a vertex to the graph
        :return: The added vertex
        """
        # self.adjacency_list = {
        # A: [C, D],
        # B: [C, F],
        # C: [A, B, E],
        # D: [A, E],
        # E: [C, D, F],
        # F: [B, E],
        # }
        new_vertex = Vertex(value)
        self.adjacency_list[new_vertex] = []
        return new_vertex

    def add_edge(self, start_vertex, end_vertex, weight=0):
        """
        Method: add edge
        Arguments: 2 vertices to be connected by the edge, weight (optional)
        Adds a new edge between two vertices in the graph
        If specified, assign a weight to the edge
        Both vertices should already be in the Graph
        :return: nothing
        """
        if start_vertex not in self.adjacency_list or end_vertex not in self.adjacency_list:
            raise KeyError()
        new_edge = Edge(end_vertex, weight)
        self.adjacency_list[start_vertex].append(new_edge)

    def get_vertices(self):
        """
        Method: get vertices
        Arguments: none
        Empty collection returned if there are no vertices
        :return: all the vertices in the graph as a collection (set, list, or similar)
        """
        return self.adjacency_list.keys()

    def get_neighbors(self, vertex):
        """
        Method: get neighbors
        Arguments: vertex
        Include the weight of the connection in the returned collection
        Empty collection returned if there are no vertices
        :return: a collection of edges connected to the given vertex
        """
        return self.adjacency_list[vertex]

    def size(self):
        """
        Method: size
        Arguments: none
        0 if there are none
        :return: the total number of vertices in the graph
        """
        return len(self.adjacency_list)



class Vertex:
    """
    AKA: Node
    Class Vertex
    Argument: value
    Instantiate: Vertex(5)
    :return: nothing
    """
    def __init__(self, value):
        self.value = value
    # property ov value


class Edge:
    """
    Class Edge
    Arguments: vertex, an optional weight
    Instantiate: Edge(vertex, 5)
    :return: nothing
    """
    def __init__(self, vertex, weight):
        self.vertex = vertex
        self.weight = weight


if __name__ == '__main__':
    graph = Graph()
    vertex = Vertex(5)

