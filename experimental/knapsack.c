#include <stdio.h>
#include <stdlib.h>
#include <time.h>

/**
 * @brief A utility function that returns the maximum of two integers.
 * @param a First integer.
 * @param b Second integer.
 * @return The larger of the two integers.
 */
int max(int a, int b) {
    return (a > b) ? a : b;
}

/**
 * @brief Solves the 0/1 knapsack problem using dynamic programming.
 * @param W The maximum capacity of the knapsack.
 * @param wt An array of weights of the items.
 * @param val An array of values of the items.
 * @param n The number of items.
 */
void solve_knapsack(int W, int wt[], int val[], int n) {
    // Allocate memory for the DP table.
    // K[i][w] will be the maximum value that can be obtained with the first
    // 'i' items and a knapsack capacity of 'w'.
    int **K = (int **)malloc((n + 1) * sizeof(int *));
    if (K == NULL) {
        fprintf(stderr, "Failed to allocate memory for DP table rows.\n");
        return;
    }
    for (int i = 0; i <= n; i++) {
        K[i] = (int *)malloc((W + 1) * sizeof(int));
        if (K[i] == NULL) {
            fprintf(stderr, "Failed to allocate memory for DP table columns.\n");
            // Free previously allocated memory before returning
            for (int j = 0; j < i; j++) free(K[j]);
            free(K);
            return;
        }
    }

    // Build the DP table K[][] in a bottom-up manner
    for (int i = 0; i <= n; i++) {
        for (int w = 0; w <= W; w++) {
            if (i == 0 || w == 0) {
                // Base case: no items or no capacity results in zero value.
                K[i][w] = 0;
            } else if (wt[i - 1] <= w) {
                // If the current item's weight is less than or equal to the current capacity 'w',
                // we have two choices:
                // 1. Include the item: value[i-1] + value from remaining capacity K[i-1][w - wt[i-1]]
                // 2. Exclude the item: value from K[i-1][w]
                K[i][w] = max(val[i - 1] + K[i - 1][w - wt[i - 1]], K[i - 1][w]);
            } else {
                // If the current item is heavier than the capacity 'w', we cannot include it.
                K[i][w] = K[i - 1][w];
            }
        }
    }
    // The result is K[n][W], but we don't need it for timing purposes.

    // Free the dynamically allocated memory
    for (int i = 0; i <= n; i++) {
        free(K[i]);
    }
    free(K);
}

int main() {
    // Seed the random number generator to get different items each run
    srand(time(NULL));

    // Define the ranges for n and W to test.
    // You can adjust these values to get more or fewer data points.
    int n_values[] = {2500, 5000, 7500, 10000, 12500, 15000, 17500, 20000};
    int w_values[] = {2500, 5000, 7500, 10000, 12500, 15000, 17500, 20000};
    int num_n_steps = sizeof(n_values) / sizeof(n_values[0]);
    int num_w_steps = sizeof(w_values) / sizeof(w_values[0]);

    // Print the CSV header for the output data
    printf("n,W,time_ms\n");

    // Loop through each combination of n and W
    for (int i = 0; i < num_n_steps; i++) {
        int n = n_values[i];
        
        for (int j = 0; j < num_w_steps; j++) {
            int W = w_values[j];

            // Dynamically allocate memory for the item properties
            int *values = (int *)malloc(n * sizeof(int));
            int *weights = (int *)malloc(n * sizeof(int));
            if (values == NULL || weights == NULL) {
                fprintf(stderr, "Memory allocation failed for items.\n");
                return 1;
            }

            // Generate random values and weights for the 'n' items
            for (int k = 0; k < n; k++) {
                values[k] = rand() % 200 + 1;    // Random value between 1 and 200
                weights[k] = rand() % (W/2) + 1; // Random weight up to half the capacity
            }
            
            // --- Time Measurement ---
            clock_t start, end;
            double cpu_time_used_ms;

            start = clock();
            solve_knapsack(W, weights, values, n);
            end = clock();

            // Calculate elapsed CPU time in milliseconds
            cpu_time_used_ms = ((double)(end - start)) / CLOCKS_PER_SEC * 1000.0;

            // Print the data in CSV format
            printf("%d,%d,%.4f\n", n, W, cpu_time_used_ms);
            
            // Ensure the output is printed immediately
            fflush(stdout);

            // Free memory for the next iteration
            free(values);
            free(weights);
        }
    }

    return 0;
}
