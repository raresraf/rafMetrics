import numpy as np

def find_best_c(n_data, y_data):
    """
    Finds the best constant 'c' for the model y = c * n * log(n) using the least squares method.

    The formula for 'c' is derived by minimizing the sum of squared errors:
    c = sum(x_i * y_i) / sum(x_i^2), where x_i = n_i * log(n_i).

    Args:
        n_data (np.ndarray): The array of problem sizes (n).
        y_data (np.ndarray): The array of corresponding time measurements (y).

    Returns:
        float: The optimal constant 'c'.
    """
    # Define the term that 'c' is multiplied by in our model.
    # We use np.log for the natural logarithm, common in complexity analysis (e.g., base e).
    x_data = n_data * np.log(n_data)
    
    # Calculate c using the least squares formula for a line through the origin.
    # This minimizes the squared difference between y_data and c*x_data.
    c = np.sum(x_data * y_data) / np.sum(x_data**2)
    
    return c

def main():
    """
    Main function to load data, compute constants, and plot results.
    """
    # --- Data from the problem ---
    # Column 1: Problem size (N)
    n_values = np.array([
        16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144
    ])

    # Last three columns of timing data
    series_1 = np.array([
        0.000002, 0.000004, 0.000010, 0.000033, 0.000059, 0.000168, 0.000186,
        0.000423, 0.000743, 0.002160, 0.003584, 0.008324, 0.019040, 0.038047, 0.081169
    ])

    series_2 = np.array([
        0.000022, 0.000019, 0.000026, 0.000059, 0.000088, 0.000238, 0.000299,
        0.001008, 0.001278, 0.003603, 0.006537, 0.010762, 0.022232, 0.047690, 0.097734
    ])

    series_3 = np.array([
        0.000001, 0.000002, 0.000006, 0.000012, 0.000033, 0.000053, 0.000117,
        0.000335, 0.000517, 0.000922, 0.001846, 0.003936, 0.0008138, 0.016575, 0.039046
    ])

    # --- Calculate the best 'c' for each series ---
    c1 = find_best_c(n_values, series_1)
    c2 = find_best_c(n_values, series_2)
    c3 = find_best_c(n_values, series_3)

    print("--- Optimal Constants 'c' for f(n) = c * n * log(n) ---")
    print(f"Series 1: c = {c1:.10f}")
    print(f"Series 2: c = {c2:.10f}")
    print(f"Series 3: c = {c3:.10f}")
    print("-" * 55)

    print("--- f(n) = c * n * log(n) ---")
    print(f"Series 1: f = {c1*n_values*np.log(n_values)}")
    print(f"Series 2: f = {c2*n_values*np.log(n_values)}")
    print(f"Series 3: f = {c3*n_values*np.log(n_values)}")
    print("-" * 55)


if __name__ == '__main__':
    main()



