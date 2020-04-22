import matplotlib.pyplot as plt
import sys

from rafComputing.ML.CustomSettings.settings import MAX_ITER, AUTO_DRIVER_DEFAULT_OUTPUT_NAME
from rafComputing.ML.features.feature_types import POWER_FEATURE_TYPE
from rafComputing.ML.snippets.MLdriver_more_graphs import LinearRegressionTrainingMoreGraphs


def get_feature_val_from_path(path):
    # Regular
    feature_val = 3
    if "28" in path:
        # Strassen
        feature_val = 2.8
    return feature_val


if __name__ == "__main__":
    if len(sys.argv) <= 1:
        print(
            "Usage v1: python3 rafComputing/ML/snippets/demo/strassen/ML_strassen_more_graphs.py <file_name1> <file_name2> <file_name3> ... "
        )
        print(
            "Usage (e.g.): python3 rafComputing/ML/snippets/demo/strassen/ML_strassen_more_graphs.py rComplexity/samples/matrix_multiplication/results/sprmcrogpu-wn13/result_n3_20200417113226 rComplexity/samples/matrix_multiplication/results/sprmcrogpu-wn13/result_n28_20200417113226"
        )
        sys.exit(-1)

    counter = 0
    for path in sys.argv:
        if path == sys.argv[0]:
            continue
        LinearRegressionTrainingMoreGraphs(
            path=path,
            alpha=1e-19,
            n_iterations=MAX_ITER,
            internal_counter=counter,
            feature_type=POWER_FEATURE_TYPE,
            feature_val=get_feature_val_from_path(path))
        counter = counter + 1

    plt.legend([
        "Regression line: Cache-friendly loop ordering",
        "Regression line: Strassen algorithm",
        "Train data: Cache-friendly loop ordering",
        "Test data:  Cache-friendly loop ordering",
        "Train data: Strassen algorithm",
        "Test data:  Strassen algorithm",
    ])

    # Return figure
    plt.savefig(AUTO_DRIVER_DEFAULT_OUTPUT_NAME)
    plt.close()
