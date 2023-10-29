// Shortest Path Algorithms - Network Graph (Directed Weighted)
// Dijkstra's Algorithm, A* Search Algorithm, Bellman-Ford Algorithm

#include <stdio.h>
#include <stdlib.h>
#include <limits.h>
#include <time.h>

#define V 200  // Number of vertices

struct Edge {
    int to, weight;
};

// Dijkstra's Algorithm
void dijkstra(const int graph[V][V], int start) {
    clock_t start_time = clock();  // Start measuring time
    int dist[V];
    int visited[V];

    for (int i = 0; i < V; i++) {
        dist[i] = INT_MAX;
        visited[i] = 0;
    }

    dist[start] = 0;

    for (int count = 0; count < V - 1; count++) {
        int u, min = INT_MAX;

        for (u = 0; u < V; u++)
            if (!visited[u] && dist[u] < min) {
                min = dist[u];
                start = u;
            }

        visited[start] = 1;

        for (int v = 0; v < V; v++) {
            if (!visited[v] && graph[start][v] && dist[start] != INT_MAX
                && (dist[start] + graph[start][v] < dist[v])) {
                dist[v] = dist[start] + graph[start][v];
            }
        }
    }

    // Print the shortest distances
    for (int i = 0; i < V; i++) {
        printf("Vertex %d: Distance = %d\n", i, dist[i]);
    }

    // Calculate runtime
    clock_t end_time = clock();
    double dijkstra_runtime = (double)(end_time - start_time) / CLOCKS_PER_SEC;
    printf("Dijkstra's Runtime: %.3f ms\n", dijkstra_runtime*1000);

}

// A* Search Algorithm
int heuristic[V];

int AStar(const int graph[V][V], int start, int goal) {
    clock_t start_time = clock();  // Start measuring time
    int g[V], f[V];
    int visited[V] = {0};

    for (int i = 0; i < V; i++) {
        g[i] = INT_MAX;
        f[i] = INT_MAX;
    }

    g[start] = 0;
    f[start] = heuristic[start];

    while (1) {
        int min = INT_MAX, current;

        for (int i = 0; i < V; i++) {
            if (!visited[i] && f[i] < min) {
                current = i;
                min = f[i];
            }
        }

        if (current == goal) {

            // Calculate runtime
            clock_t end_time = clock();
            double astar_runtime = (double)(end_time - start_time) / CLOCKS_PER_SEC;
            printf("A* Search Runtime: %.3f ms\n", astar_runtime*1000);

            return g[goal];
        }

        visited[current] = 1;

        for (int i = 0; i < V; i++) {
            if (!visited[i] && graph[current][i] && g[current] != INT_MAX) {
                int tentative_g = g[current] + graph[current][i];
                if (tentative_g < g[i]) {
                    g[i] = tentative_g;
                    f[i] = g[i] + heuristic[i];
                }
            }
        }
    }
}

// Bellman-Ford Algorithm
void bellmanFord(const int graph[V][V], int start) {
    clock_t start_time = clock();  // Start measuring time
    int dist[V];

    for (int i = 0; i < V; i++) {
        dist[i] = INT_MAX;
    }

    dist[start] = 0;

    for (int count = 0; count < V - 1; count++) {
        for (int u = 0; u < V; u++) {
            for (int v = 0; v < V; v++) {
                if (graph[u][v] && dist[u] != INT_MAX && (dist[u] + graph[u][v] < dist[v])) {
                    dist[v] = dist[u] + graph[u][v];
                }
            }
        }
    }

    // Check for negative weight cycles
    for (int u = 0; u < V; u++) {
        for (int v = 0; v < V; v++) {
            if (graph[u][v] && dist[u] != INT_MAX && (dist[u] + graph[u][v] < dist[v])) {
                printf("Graph contains negative weight cycle!\n");
                return;
            }
        }
    }

    // Print the shortest distances
    for (int i = 0; i < V; i++) {
        printf("Vertex %d: Distance = %d\n", i, dist[i]);
    }

    // Calculate runtime
    clock_t end_time = clock();
    double bellmanford_runtime = (double)(end_time - start_time) / CLOCKS_PER_SEC;
    printf("Bellman-Ford Runtime: %.3f ms\n", bellmanford_runtime*1000);

}

int main() {
    // Define the undirected weighted graph with edges and weights
    int graph[V][V];

    // Initialize random number generator
    srand(time(NULL));

    // Generate a random directed weighted graph
    for (int i = 0; i < V; i++) {
        for (int j = 0; j < V; j++) {
            if (i == j) {
                graph[i][j] = 0;  // No self-loops
            } else {
                // Generate random edge weights between 0 and 20
                graph[i][j] = rand() % 21;
            }
        }
    }

    // Set your heuristic values for A* using Manhattan Distance
    int goal = 186;
    for (int i = 0; i < V; i++) {
        int dx = abs(i - goal);
        int dy = abs(goal - 9); // Assuming the goal is at vertex 9
        heuristic[i] = dx + dy;
    }

    int start = 0;

    printf("Weighted Graph:\n");
    for (int i = 0; i < V; i++) {
        for (int j = 0; j < V; j++) {
            printf("%d\t", graph[i][j]);
        }
        printf("\n");
    }

    printf("\nDijkstra's Algorithm:\n");
    dijkstra(graph, start);

    printf("\nA* Search Algorithm:\n");
    int astar_result = AStar(graph, start, goal);
    printf("Shortest Path from %d to %d: %d\n", start, goal, astar_result);

    printf("\nBellman-Ford Algorithm:\n");
    bellmanFord(graph, start);

    return 0;
}
