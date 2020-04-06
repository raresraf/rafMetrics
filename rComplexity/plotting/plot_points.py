import matplotlib.pyplot as plt
import numpy as np
import sys

from rComplexity.plotting.constants import pool_plotting_points_symbols


def plot_points_from_file(filename, matrixCols):
    # Load Matrix
    matrix = np.loadtxt(filename, usecols=range(matrixCols + 1))

    for i in range(1, matrixCols + 1):
        plt.plot(matrix[:, 0],
                 matrix[:, i],
                 next(pool_plotting_points_symbols),
                 label="Sample: " + str(i))

    plt.legend()
    plt.show()


if __name__ == "__main__":
    if len(sys.argv) <= 2:
        print("Usage: python3 plot_points.py <file_name> <matrixCols>")
        sys.exit(-1)

    plot_points_from_file(sys.argv[1], int(sys.argv[2]))
