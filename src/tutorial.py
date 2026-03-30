from src.graph import create_graph, get_degree, dfs_traversal, bfs_traversal, find_shortest_path, visualize_graph

# Contoh edges
edges = [(1, 2), (1, 3), (2, 4), (3, 5), (4, 5)]

# Buat graf
G = create_graph(edges)

# Test fungsi
print("Degree node 1:", get_degree(G, 1))
print("DFS dari 1:", dfs_traversal(G, 1))
print("BFS dari 1:", bfs_traversal(G, 1))
print("Shortest path 1 ke 5:", find_shortest_path(G, 1, 5))

# Visualisasi graf
visualize_graph(G)
