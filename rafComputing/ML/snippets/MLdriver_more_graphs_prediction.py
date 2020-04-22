import matplotlib.pyplot as plt
import sys
from sklearn.metrics import mean_squared_error, r2_score

from rafComputing.ML.CustomSettings.settings import (
    MAX_ITER,
    ALPHA,
    MAX_ITER_LinearRegressionTraining,
    ALPHA_LinearRegressionTraining,
    AUTO_DRIVER_DEFAULT_OUTPUT_NAME,
)
from rafComputing.ML.RegressionEngine.LinearRegressionGD import LinearRegressionGD
from rafComputing.ML.features.feature_types import (
    NO_FEATURE_TYPE,
    POWER_FEATURE_TYPE,
)
from rafComputing.ML.helpers.generate_larger_evaluation_set import generate_larger_evaluation_set
from rafComputing.ML.helpers.load_data import matrix_to_train_test_w_generate_larger_evaluation_set

LINE_COLORS = ["blue", "orange", "green"]

# Light
TRAIN_POINT_COLORS = ["#ADD8E6", "#FFCF9E", "#90ee90"]
# Dark
TEST_POINT_COLORS = ["#00008B", "#b36200", "#006400"]


def LinearRegressionTrainingMoreGraphsPrediction(
    path,
    alpha=ALPHA_LinearRegressionTraining,
    n_iterations=MAX_ITER_LinearRegressionTraining,
    internal_counter=0,
    feature_type=NO_FEATURE_TYPE,
    feature_val=1.0,
    first=True,
    final=False,
    plt_legend=None,
    custom_generate_larger_evaluation_set=generate_larger_evaluation_set,
):
    (x, orig_x), y, (X_train, orig_x_train), (
        X_test,
        orig_x_test,
    ), y_train, y_test, (
        X_test2,
        orig_x_test2) = matrix_to_train_test_w_generate_larger_evaluation_set(
            path=path,
            feature_type=feature_type,
            feature_val=feature_val,
            custom_generate_larger_evaluation_set=
            custom_generate_larger_evaluation_set)

    # Model initialization
    regression_model = LinearRegressionGD(alpha, n_iterations)
    regression_model.fit(X_train, y_train)
    print(regression_model.w_.flatten())

    y_predicted = regression_model.predict(x)
    y_predicted_train = regression_model.predict(X_train)
    y_predicted_test = regression_model.predict(X_test)

    # Predict generated sets
    y_predicted_test2 = regression_model.predict(X_test2)

    # Model evaluation training data
    rmse = mean_squared_error(y_train, y_predicted_train)
    r2 = r2_score(y_train, y_predicted_train)
    print("[Training Set] Root mean squared error: ", rmse)
    print("[Training Set] R2 score: ", r2)

    # Model evaluation test data
    rmse = mean_squared_error(y_test, y_predicted_test)
    r2 = r2_score(y_test, y_predicted_test)
    print("[Test Set] Root mean squared error: ", rmse)
    print("[Test Set] R2 score: ", r2)

    orig_y_train = y_train.flatten()
    orig_y_test = y_test.flatten()

    if first:
        plt.vlines(x=orig_x_test2[0],
                   ymin=min(min(y_predicted), min(y_predicted_test2)),
                   ymax=max(max(y_predicted), max(y_predicted_test2)),
                   linestyle="--")

    # Data points
    plt.scatter(orig_x, y, s=12, color=TRAIN_POINT_COLORS[internal_counter])

    plt.scatter(orig_x_test2,
                y_predicted_test2,
                marker='x',
                s=16,
                color=TEST_POINT_COLORS[internal_counter])

    plt.xlabel("Input size")
    plt.ylabel("Time (seconds)")

    # Plotting predicted values
    orig_x = orig_x.flatten()

    # Predicted values
    y_predicted = y_predicted.flatten()
    plt.plot(orig_x, y_predicted, color=LINE_COLORS[internal_counter])
    plt.plot(orig_x_test2,
             y_predicted_test2,
             color=LINE_COLORS[internal_counter],
             linestyle="--")

    if final:
        plt.legend(plt_legend, fontsize=6)

        # Return figure
        plt.savefig(AUTO_DRIVER_DEFAULT_OUTPUT_NAME)
        plt.close()


if __name__ == "__main__":
    if len(sys.argv) <= 1:
        print(
            "Usage v1: python3 MLdriver_more_graphs_prediction.py <file_name1> <file_name2> <file_name3> ... "
        )
        print(
            "Usage (e.g.): python3 rafComputing/ML/snippets/MLdriver_more_graphs_prediction.py rComplexity/samples/matrix_multiplication/results/fsri5/result_n3_0_20200309165609 rComplexity/samples/matrix_multiplication/results/fsri5/result_n3_2_20200309165609 rComplexity/samples/matrix_multiplication/results/fsri5/result_n3_3_20200309165609             "
        )
        sys.exit(-1)

    plt_legend = [
        "Regression line(Dataset) \nNaive Matrix Multiplication",
        "Regression line(Prediction) \nNaive Matrix Multiplication",
        "Regression line(Dataset) \nCache-friendly loop ordering",
        "Regression line(Prediction) \nCache-friendly loop ordering",
        "Regression line(Dataset) \nBlocked Matrix Multiplication",
        "Regression line(Prediction) \nBlocked Matrix Multiplication",
        "Separation line\nDataset (left)\nGeneralization (right)",
        "Dataset entry: Naive Matrix Multiplication",
        "Generated data: Naive Matrix Multiplication",
        "Dataset entry: Cache-friendly loop ordering",
        "Generated data: Cache-friendly loop ordering",
        "Dataset entry: Blocked Matrix Multiplication",
        "Generated data: Blocked Matrix Multiplication",
    ]

    counter = 0
    for path in sys.argv:
        if path == sys.argv[0]:
            continue

        LinearRegressionTrainingMoreGraphsPrediction(
            path=path,
            alpha=ALPHA,
            n_iterations=MAX_ITER,
            internal_counter=counter,
            feature_type=POWER_FEATURE_TYPE,
            feature_val=3.0,
            first=(path == sys.argv[1]),
            final=(path == sys.argv[len(sys.argv) - 1]),
            plt_legend=plt_legend,
            custom_generate_larger_evaluation_set=generate_larger_evaluation_set
        )

        counter = counter + 1
