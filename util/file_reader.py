from graphs.graph import Graph


def read_graph_from_file(filename):
    """
    Read in data from the specified filename, and create and return a graph
    object corresponding to that data.

    Arguments:
    filename (string): The relative path of the file to be processed

    Returns:
    Graph: A directed or undirected Graph object containing the specified
    vertices and edges
    """
     my_file = open(filename)

    graph_type = my_file.readline().strip()
    if graph_type == "G" :
        graph = Graph(False)
    elif graph_type == "D" :
        graph = Graph(True)
    else:
        raise ValueError("Unexpected character")

    vertices = my_file.readline().strip().split(",")
    for vertex in vertices:
        graph.add_vertex(vertex)


    for edge in my_file:
        vertex1, vertex2 = edge.strip()[1:-1].split(",")
        graph.add_edge(vertex1, vertex2)

    return graph

    pass

if __name__ == '__main__':

    graph = read_graph_from_file('test.txt')

    print(graph)