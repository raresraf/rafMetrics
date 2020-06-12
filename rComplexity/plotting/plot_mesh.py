import matplotlib.pyplot as plt
import numpy as np
import sys

if __name__ == "__main__":
    #python3 rComplexity/plotting/plot_mesh.py rComplexity/samples/gym-chess-master/results/macOS/PYTHON_chess_results_20200603145240
    if len(sys.argv) != 2:
        print("Usage: python3 plot_mesh.py <file_name>")
        sys.exit(-1)

    path = sys.argv[1]
    matrix = np.loadtxt(path, usecols=range(3))

    X3D = matrix[:, 0]
    Y3D = matrix[:, 1]
    Z = matrix[:, 2].reshape(len(set(X3D)), len(set(Y3D)))

    X3D = X3D.reshape(Z.shape)
    Y3D = Y3D.reshape(Z.shape)

    print(X3D)
    print(Y3D)
    print(Z)

    fig = plt.figure()
    ax = plt.axes(projection='3d')
    ax.plot_surface(X3D,
                    Y3D,
                    Z,
                    rstride=1,
                    cstride=1,
                    cmap='viridis',
                    edgecolor='none')
    ax.set_title("Chess game simulation")
    ax.set_xlabel("num_episodes")
    ax.set_ylabel("num_steps_per_episode")
    ax.set_zlabel("Total time (seconds)")

    plt.show()
