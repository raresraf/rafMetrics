import io
import csv
import numpy as np
import math

def generate_latex_tikz(n: np.ndarray, W: np.ndarray, y: np.ndarray, r: float) -> str:
    """
    Generates LaTeX code for a 3D pgfplots graph of the data and the fitted surface.

    Args:
        n: NumPy array of the number of items.
        W: NumPy array of the knapsack capacities.
        y: NumPy array of the dependent variable (time_ms).
        r: The calculated constant of proportionality.

    Returns:
        A string containing the complete LaTeX code for the figure.
    """
    # Convert time from milliseconds to seconds for the plot
    y_seconds = y / 1000.0

    # Format the coordinates for the 3D scatter plot
    coords_data_3d = " ".join([f"({ni}, {Wi}, {yi_s:.8f})" for ni, Wi, yi_s in zip(n, W, y_seconds)])

    # Format the constant 'r' into scientific notation for the legend
    try:
        exponent = math.floor(math.log10(abs(r)))
        mantissa = r / (10**exponent)
        r_latex = f"$r={mantissa:.3f} \\cdot 10^{{{exponent}}}$"
    except ValueError:
        r_latex = f"$r={r:.3f}$"

    # Define the range for the surface plot based on the data
    n_min, n_max = np.min(n), np.max(n)
    w_min, w_max = np.min(W), np.max(W)

    # The function for the surface plot is r * x * y, where time is in seconds
    surface_function = f"{{{r / 1000.0} * x * y}}"

    # Assemble the final LaTeX string for a 3D plot
    latex_output = f"""
\\begin{{figure}}[h!]
\\centering
\\begin{{tikzpicture}}
    \\begin{{axis}}[
        title={{Knapsack Execution Time vs. n and W}},
        xlabel={{$n$ (Number of Items)}},
        ylabel={{$W$ (Capacity)}},
        zlabel={{Time (seconds)}},
        legend pos=north west,
        grid=major,
        width=16cm,
        height=12cm,
        view={{60}}{{30}},
        zticklabel style={{/pgf/number format/fixed, /pgf/number format/precision=2}},
    ]

    % 3D Scatter plot for the actual measured data
    \\addplot3[
        only marks,
        color=blue,
        mark=*,
    ] coordinates {{
        {coords_data_3d}
    }};
    \\addlegendentry{{Measured Data}}

    % Fitted surface representing time = r * n * W
    \\addplot3[
        surf,
        color=red,
        opacity=0.7,
        domain={n_min}:{n_max},
        domain y={w_min}:{w_max},
        samples=15,
        z buffer=sort,
    ] {surface_function};
    \\addlegendentry{{{r_latex}}}

    \\end{{axis}}
\\end{{tikzpicture}}
\\caption{{3D plot of the 0/1 Knapsack algorithm performance. The execution time (z-axis) is plotted against the number of items ($n$) and the knapsack capacity ($W$). The data points closely follow the fitted surface defined by $time = r \\cdot n \\cdot W$, visualizing the $O(n \\cdot W)$ complexity.}}
\\label{{fig:knapsack-complexity-3d}}
\\end{{figure}}
"""
    return latex_output

def process_data_and_generate_latex(data: str):
    """
    Parses CSV data, calculates the best 'r', and prints the LaTeX code.

    Args:
        data: A string containing the CSV data with columns n, W, and time_ms.
    """
    # Use io.StringIO to treat the string data as a file
    data_file = io.StringIO(data)
    
    # Read the CSV data, skipping the header
    reader = csv.reader(data_file)
    header = next(reader)
    
    # Load data into lists and convert to NumPy arrays for efficient computation
    n_vals, w_vals, time_ms_vals = [], [], []
    for row in reader:
        n_vals.append(int(row[0]))
        w_vals.append(int(row[1]))
        time_ms_vals.append(float(row[2]))

    n = np.array(n_vals)
    W = np.array(w_vals)
    time_ms = np.array(time_ms_vals)

    # --- Find the best 'r' using the least squares method ---
    # Model: y = r * x, where y is time_ms and x is (n * W).
    # Solution: r = Σ(x_i * y_i) / Σ(x_i^2)
    x_combined = n * W
    y = time_ms
    
    numerator = np.sum(x_combined * y)
    denominator = np.sum(x_combined * x_combined)
    
    r = 0.0 if denominator == 0 else numerator / denominator
    
    # --- Generate and print the LaTeX output ---
    latex_code = generate_latex_tikz(n, W, time_ms, r)
    print(latex_code)


# The data you provided
csv_data = """n,W,time_ms
2500,2500,48.9010
2500,5000,92.7970
2500,7500,139.9630
2500,10000,203.9360
2500,12500,221.5770
2500,15000,258.6120
2500,17500,320.5740
2500,20000,328.1810
5000,2500,97.2550
5000,5000,188.1200
5000,7500,279.1970
5000,10000,406.1400
5000,12500,479.6660
5000,15000,577.0370
5000,17500,637.3480
5000,20000,750.3690
7500,2500,142.2620
7500,5000,281.9770
7500,7500,419.4900
7500,10000,576.7760
7500,12500,714.5260
7500,15000,823.3670
7500,17500,988.1020
7500,20000,1116.7110
10000,2500,189.0950
10000,5000,375.1150
10000,7500,561.3980
10000,10000,781.7830
10000,12500,968.0090
10000,15000,1119.5780
10000,17500,1341.5330
10000,20000,1540.0570
12500,2500,232.5560
12500,5000,466.7170
12500,7500,701.5510
12500,10000,972.0270
12500,12500,1227.8950
12500,15000,1452.2500
12500,17500,1728.8990
12500,20000,1935.0700
15000,2500,277.1650
15000,5000,570.4730
15000,7500,847.5410
15000,10000,1172.1750
15000,12500,1457.2540
15000,15000,1727.3870
15000,17500,2010.5060
15000,20000,2260.7020
17500,2500,322.8220
17500,5000,661.3950
17500,7500,975.4770
17500,10000,1336.8760
17500,12500,1694.5290
17500,15000,1986.1460
17500,17500,2318.9990
17500,20000,2639.5560
20000,2500,370.0470
20000,5000,747.8700
20000,7500,1117.0620
20000,10000,1506.6010
20000,12500,1897.6520
20000,15000,2255.8310
20000,17500,2743.8880
20000,20000,3039.6860
"""

if __name__ == "__main__":
    process_data_and_generate_latex(csv_data)


