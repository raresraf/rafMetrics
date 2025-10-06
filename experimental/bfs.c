#include <stdio.h>
#include <stdlib.h>
#include <time.h>

// --- Data Structures ---

// A node in the adjacency list
typedef struct AdjListNode {
    int dest;
    struct AdjListNode* next;
} AdjListNode;

// The adjacency list for a single vertex
typedef struct AdjList {
    AdjListNode *head;
} AdjList;

// The graph structure
typedef struct Graph {
    int V; // Number of vertices
    AdjList* array;
} Graph;

// A queue for the BFS algorithm
typedef struct Queue {
    int front, rear, size;
    unsigned capacity;
    int* array;
} Queue;


// --- Queue Utility Functions ---

// Creates a new queue of a given capacity
Queue* createQueue(unsigned capacity) {
    Queue* queue = (Queue*) malloc(sizeof(Queue));
    queue->capacity = capacity;
    queue->front = queue->size = 0;
    queue->rear = capacity - 1;
    queue->array = (int*) malloc(queue->capacity * sizeof(int));
    return queue;
}

// Checks if the queue is full
int isFull(Queue* queue) {
    return (queue->size == queue->capacity);
}

// Checks if the queue is empty
int isEmpty(Queue* queue) {
    return (queue->size == 0);
}

// Adds an item to the queue
void enqueue(Queue* queue, int item) {
    if (isFull(queue))
        return;
    queue->rear = (queue->rear + 1) % queue->capacity;
    queue->array[queue->rear] = item;
    queue->size = queue->size + 1;
}

// Removes an item from the queue
int dequeue(Queue* queue) {
    if (isEmpty(queue))
        return -1;
    int item = queue->array[queue->front];
    queue->front = (queue->front + 1) % queue->capacity;
    queue->size = queue->size - 1;
    return item;
}

// --- Graph Utility Functions ---

// Creates a new adjacency list node
AdjListNode* newAdjListNode(int dest) {
    AdjListNode* newNode = (AdjListNode*) malloc(sizeof(AdjListNode));
    newNode->dest = dest;
    newNode->next = NULL;
    return newNode;
}

// Creates a graph with V vertices
Graph* createGraph(int V) {
    Graph* graph = (Graph*) malloc(sizeof(Graph));
    graph->V = V;
    // Create an array of adjacency lists
    graph->array = (AdjList*) malloc(V * sizeof(AdjList));
    // Initialize each adjacency list as empty
    for (int i = 0; i < V; ++i)
        graph->array[i].head = NULL;
    return graph;
}

// Adds an edge to an undirected graph
void addEdge(Graph* graph, int src, int dest) {
    // Add an edge from src to dest
    AdjListNode* newNode = newAdjListNode(dest);
    newNode->next = graph->array[src].head;
    graph->array[src].head = newNode;

    // Add an edge from dest to src
    newNode = newAdjListNode(src);
    newNode->next = graph->array[dest].head;
    graph->array[dest].head = newNode;
}

// Frees the memory allocated for the graph
void freeGraph(Graph* graph) {
    if (!graph) return;
    for (int v = 0; v < graph->V; ++v) {
        AdjListNode* pCrawl = graph->array[v].head;
        while (pCrawl) {
            AdjListNode* temp = pCrawl;
            pCrawl = pCrawl->next;
            free(temp);
        }
    }
    free(graph->array);
    free(graph);
}


// --- Breadth-First Search (BFS) ---

// Performs BFS traversal from a given source vertex
void BFS(Graph* graph, int startVertex) {
    // Allocate visited array and initialize to false
    int* visited = (int*)malloc(graph->V * sizeof(int));
    for (int i = 0; i < graph->V; i++)
        visited[i] = 0;

    // Create a queue for BFS
    Queue* queue = createQueue(graph->V);

    // Mark the current node as visited and enqueue it
    visited[startVertex] = 1;
    enqueue(queue, startVertex);

    while (!isEmpty(queue)) {
        // Dequeue a vertex from queue
        int currentVertex = dequeue(queue);

        // Get all adjacent vertices of the dequeued vertex
        AdjListNode* temp = graph->array[currentVertex].head;
        while (temp) {
            int adjVertex = temp->dest;
            if (!visited[adjVertex]) {
                visited[adjVertex] = 1;
                enqueue(queue, adjVertex);
            }
            temp = temp->next;
        }
    }

    // Free allocated memory
    free(visited);
    free(queue->array);
    free(queue);
}

// --- Main Driver ---

int main() {
    // Seed the random number generator
    srand(time(NULL));

    // Define the configurations to test
    // Each row is {num_vertices, num_edges_multiplier}
    // num_edges = num_vertices * num_edges_multiplier
    int configs[][2] = {
        {1000000, 1},  {1000000, 2},  {1000000, 3},  {1000000, 4},  {1000000, 5},
        {2000000, 1},  {2000000, 2},  {2000000, 3},  {2000000, 4},  {2000000, 5},
        {3000000, 1},  {3000000, 2},  {3000000, 3},  {3000000, 4},  {3000000, 5},
        {4000000, 1},  {4000000, 2},  {4000000, 3},  {4000000, 4},  {4000000, 5},
        {5000000, 1},  {5000000, 2},  {5000000, 3},  {5000000, 4},  {5000000, 5},
    };
    int num_configs = sizeof(configs) / sizeof(configs[0]);

    // Print CSV header
    printf("Vertices (V),Edges (E),Time (seconds)\n");

    // Loop through each configuration
    for (int i = 0; i < num_configs; ++i) {
        int V = configs[i][0];
        int E = V * configs[i][1];

        // Create a graph
        Graph* graph = createGraph(V);

        // Add E random edges.
        // Note: This may create duplicate edges, but for the purpose of
        // complexity analysis on large graphs, the impact is minimal.
        for (int j = 0; j < E; ++j) {
            int u = rand() % V;
            int v = rand() % V;
            if (u != v) { // Avoid self-loops
                addEdge(graph, u, v);
            }
        }

        // Measure execution time of BFS
        clock_t start = clock();
        BFS(graph, 0); // Start BFS from vertex 0
        clock_t end = clock();

        double time_spent = (double)(end - start) / CLOCKS_PER_SEC;

        // Print the results in CSV format
        printf("%d,%d,%.6f\n", V, E, time_spent);

        // Free the graph memory for the next iteration
        freeGraph(graph);
    }

    return 0;
}


