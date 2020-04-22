import numpy as np
import sys

from rafComputing.ML.CustomSettings.settings import MAX_ITER
from rafComputing.ML.features.feature_types import POWER_FEATURE_TYPE
from rafComputing.ML.snippets.demo.strassen.CustomStrassenLinearRegressionTrainingMoreGraphsPrediction import \
    CustomStrassenLinearRegressionTrainingMoreGraphsPrediction
from rafComputing.ML.snippets.demo.strassen.ML_strassen_more_graphs import get_feature_val_from_path


def strassen_generate_larger_evaluation_set(x):
    latest_element = np.max(x)
    extra_x = np.linspace(latest_element, 1e8, num=100)
    return extra_x


if __name__ == "__main__":
    if len(sys.argv) <= 1:
        print(
            "Usage v1: python3 rafComputing/ML/snippets/demo/strassen/ML_strassen_more_graphs_prediction.py <file_name1> <file_name2> <file_name3> ... "
        )
        print(
            "Usage (e.g.): python3 rafComputing/ML/snippets/demo/strassen/ML_strassen_more_graphs_prediction.py rComplexity/samples/matrix_multiplication/results/sprmcrogpu-wn13/result_n3_20200417113226 rComplexity/samples/matrix_multiplication/results/sprmcrogpu-wn13/result_n28_20200417113226"
        )
        sys.exit(-1)

    plt_legend = [
        "Regression line(Prediction) \nRegression line: Cache-friendly loop ordering",
        "Regression line(Prediction) \nRegression line: Strassen algorithm",
        "Generated data:  Cache-friendly loop ordering",
        "Generated data:  Strassen algorithm",
    ]

    counter = 0
    for path in sys.argv:
        if path == sys.argv[0]:
            continue
        CustomStrassenLinearRegressionTrainingMoreGraphsPrediction(
            path=path,
            alpha=1e-19,
            n_iterations=MAX_ITER,
            internal_counter=counter,
            feature_type=POWER_FEATURE_TYPE,
            feature_val=get_feature_val_from_path(path),
            first=(path == sys.argv[1]),
            final=(path == sys.argv[len(sys.argv) - 1]),
            plt_legend=plt_legend,
            custom_generate_larger_evaluation_set=
            strassen_generate_larger_evaluation_set)
        counter = counter + 1
