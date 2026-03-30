import networkx as nx
from collections import deque
import matplotlib.pyplot as plt

# 1. Membuat graf dari daftar edge
def create_graph(edges: list[tuple[int, int]]) -> nx.Graph:
    G = nx.Graph()
    G.add_edges_from(edges)
    return G

# 2. Menghitung derajat simpul
def get_degree(G: nx.Graph, node: int) -> int:
    return G.degree(node)

# 3. DFS Traversal
def dfs_traversal(G: nx.Graph, start: int) -> list[int]:
    visited = []
    stack = [start]

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            neighbors = sorted(G.neighbors(node), reverse=True)
            for neighbor in neighbors:
                if neighbor not in visited:
                    stack.append(neighbor)
    return visited

# 4. BFS Traversal
def bfs_traversal(G: nx.Graph, start: int) -> list[int]:
    visited = []
    queue = deque([start])

    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.append(node)
            neighbors = sorted(G.neighbors(node))
            for neighbor in neighbors:
                if neighbor not in visited:
                    queue.append(neighbor)
    return visited

# 5. Shortest Path
def find_shortest_path(G: nx.Graph, source: int, target: int) -> list[int]:
    return nx.shortest_path(G, source=source, target=target)

# 6. Visualisasi Graf
def visualize_graph(G: nx.Graph) -> None:
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True)
    plt.savefig("graph.png")
    plt.close()
