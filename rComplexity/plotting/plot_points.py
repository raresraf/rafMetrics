import matplotlib.pyplot as plt
import numpy as np
import sys

from rComplexity.plotting.constants import pool_plotting_points_symbols

CONFIG = {
    1: "Naive Matrix Multiplication",
    2: "Cache-friendly loop ordering",
    3: "Blocked Matrix Multiplication",
}


def plot_points_from_file(filename, matrixCols):
    # Load Matrix
    matrix = np.loadtxt(filename, usecols=range(matrixCols + 1))

    for i in range(1, matrixCols + 1):
        name = CONFIG.get(i, str(i))
        plt.plot(
            matrix[:, 0],
            matrix[:, i],
            next(pool_plotting_points_symbols),
            label="Sample: " + name,
        )

    plt.legend()
    plt.show()


if __name__ == "__main__":
    if len(sys.argv) <= 2:
        print("Usage: python3 plot_points.py <file_name> <matrixCols>")
        sys.exit(-1)

    plot_points_from_file(sys.argv[1], int(sys.argv[2]))
