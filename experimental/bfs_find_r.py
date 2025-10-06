import io
import csv
import numpy as np
import math

def generate_latex_tikz(V: np.ndarray, E: np.ndarray, y: np.ndarray, r: float) -> str:
    """
    Generates LaTeX code for a 3D pgfplots graph of the BFS data and the fitted surface.

    Args:
        V: NumPy array of the number of vertices.
        E: NumPy array of the number of edges.
        y: NumPy array of the dependent variable (time_seconds).
        r: The calculated constant of proportionality.

    Returns:
        A string containing the complete LaTeX code for the figure.
    """
    # Format the coordinates for the 3D scatter plot
    coords_data_3d = " ".join([f"({vi}, {ei}, {yi:.8f})" for vi, ei, yi in zip(V, E, y)])

    # Format the constant 'r' into scientific notation for the legend
    try:
        exponent = math.floor(math.log10(abs(r)))
        mantissa = r / (10**exponent)
        r_latex = f"$r={mantissa:.3f} \\cdot 10^{{{exponent}}}$"
    except (ValueError, OverflowError):
        r_latex = f"$r={r:.3g}$"

    # Define the range for the surface plot based on the data
    v_min, v_max = np.min(V), np.max(V)
    e_min, e_max = np.min(E), np.max(E)

    # The function for the surface plot is r * (V + E), which is r * (x + y) in pgfplots
    surface_function = f"{{{r} * (x + y)}}"

    # Assemble the final LaTeX string for a 3D plot
    latex_output = f"""
\\begin{{figure}}[h!]
\\centering
\\begin{{tikzpicture}}
    \\begin{{axis}}[
        title={{BFS Execution Time vs. Vertices and Edges}},
        xlabel={{$V$ (Number of Vertices)}},
        ylabel={{$E$ (Number of Edges)}},
        zlabel={{Time (seconds)}},
        legend pos=north west,
        grid=major,
        width=16cm,
        height=12cm,
        view={{60}}{{30}},
        zticklabel style={{/pgf/number format/fixed, /pgf/number format/precision=2}},
        yticklabel style={{/pgf/number format/sci}},
        xticklabel style={{/pgf/number format/sci}},
    ]

    % 3D Scatter plot for the actual measured BFS data
    \\addplot3[
        only marks,
        color=green,
        mark=*,
    ] coordinates {{
        {coords_data_3d}
    }};
    \\addlegendentry{{Measured BFS Data}}

    % Fitted surface representing time = r * (V + E)
    \\addplot3[
        surf,
        color=orange,
        opacity=0.7,
        domain={v_min}:{v_max},
        domain y={e_min}:{e_max},
        samples=15,
        z buffer=sort,
    ] {surface_function};
    \\addlegendentry{{{r_latex}}}

    \\end{{axis}}
\\end{{tikzpicture}}
\\caption{{3D plot of the Breadth-First Search (BFS) algorithm performance. The execution time (z-axis) is plotted against the number of vertices ($V$) and edges ($E$). The data points closely follow the fitted plane defined by $time = r \\cdot (V + E)$, visualizing the $O(V + E)$ complexity.}}
\\label{{fig:bfs-complexity-3d}}
\\end{{figure}}
"""
    return latex_output

def process_data_and_generate_latex(data: str):
    """
    Parses CSV data, calculates the best 'r' for BFS, and prints the LaTeX code.

    Args:
        data: A string containing the CSV data with columns V, E, and time.
    """
    # Use io.StringIO to treat the string data as a file
    data_file = io.StringIO(data)
    
    # Read the CSV data, skipping the header
    reader = csv.reader(data_file)
    header = next(reader)
    
    # Load data into lists and convert to NumPy arrays for efficient computation
    v_vals, e_vals, time_vals = [], [], []
    for row in reader:
        v_vals.append(int(row[0]))
        e_vals.append(int(row[1]))
        time_vals.append(float(row[2]))

    V = np.array(v_vals)
    E = np.array(e_vals)
    time_seconds = np.array(time_vals)

    # --- Find the best 'r' using the least squares method ---
    # Model: y = r * x, where y is time_seconds and x is (V + E).
    # Solution: r = Σ(x_i * y_i) / Σ(x_i^2)
    x_combined = V + E
    y = time_seconds
    
    numerator = np.sum(x_combined * y)
    denominator = np.sum(x_combined * x_combined)
    
    r = 0.0 if denominator == 0 else numerator / denominator
    
    # --- Generate and print the LaTeX output ---
    latex_code = generate_latex_tikz(V, E, time_seconds, r)
    print(latex_code)


# The data for BFS performance
csv_data = """Vertices (V),Edges (E),Time (seconds)
1000000,1000000,0.234274
1000000,2000000,0.403702
1000000,3000000,0.552781
1000000,4000000,0.747199
1000000,5000000,0.966431
2000000,2000000,0.006395
2000000,4000000,0.805063
2000000,6000000,1.215489
2000000,8000000,1.605980
2000000,10000000,2.089497
3000000,3000000,0.738303
3000000,6000000,1.338934
3000000,9000000,1.821428
3000000,12000000,2.484839
3000000,15000000,3.312580
4000000,4000000,1.020870
4000000,8000000,1.710339
4000000,12000000,2.522506
4000000,16000000,3.412965
4000000,20000000,4.435482
5000000,5000000,0.009743
5000000,10000000,2.197207
5000000,15000000,3.345080
5000000,20000000,4.339670
5000000,25000000,5.638347
"""

if __name__ == "__main__":
    process_data_and_generate_latex(csv_data)



