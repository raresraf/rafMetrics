import matplotlib.pyplot as plt
import numpy as np
import sys
from numpy.polynomial import Polynomial as P
from sklearn.metrics import mean_squared_error, r2_score

from rafComputing.ML.CustomSettings.settings import (
    MAX_ITER,
    ALPHA,
    DEFAULT_ITER_INCREASE_STEPS_LOG,
    DEFAULT_ITER_INCREASE_STEPS,
    DEFAULT_RANGE_,
    MAX_ITER_LinearRegressionTraining,
    ALPHA_LinearRegressionTraining,
    OUTPUT_PREFIX,
    OUTPUT_PREFIX_0,
)
from rafComputing.ML.RegressionEngine.LinearRegressionGD import LinearRegressionGD
from rafComputing.ML.features.feature_types import (
    POLYNOMIAL_FEATURE_TYPE,
    NO_FEATURE_TYPE,
)
from rafComputing.ML.helpers.load_data import matrix_to_train_test
from rafComputing.ML.helpers.polynomial_to_latex import polynomial_to_LaTeX


def LinearRegressionTraining(
    path,
    alpha=ALPHA_LinearRegressionTraining,
    n_iterations=MAX_ITER_LinearRegressionTraining,
    output_name=OUTPUT_PREFIX_0,
    feature_type=NO_FEATURE_TYPE,
    feature_val=1,
):
    (x, orig_x), y, (X_train, orig_x_train), (
        X_test,
        orig_x_test,
    ), y_train, y_test = matrix_to_train_test(path=path,
                                              feature_type=feature_type,
                                              feature_val=feature_val)

    # Model initialization
    regression_model = LinearRegressionGD(alpha, n_iterations)
    regression_model.fit(X_train, y_train)

    # Predict
    y_predicted = regression_model.predict(x)
    y_predicted_train = regression_model.predict(X_train)
    y_predicted_test = regression_model.predict(X_test)

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

    # Data points
    plt.scatter(orig_x_train, orig_y_train, s=20, color="b")
    plt.scatter(orig_x_test, orig_y_test, s=40, color="r")
    plt.xlabel("Input size")
    plt.ylabel("Time (seconds)")

    # Plotting predicted values
    orig_x = orig_x.flatten()

    # Predicted values
    y_predicted = y_predicted.flatten()
    plt.plot(orig_x, y_predicted, color="g")
    plt.legend(["Regression line", "Train data", "Test data"])
    plt.title(polynomial_to_LaTeX(P(regression_model.w_.flatten())))

    # Return figure
    plt.savefig(output_name)

    plt.close()


if __name__ == "__main__":
    if len(sys.argv) <= 1:
        print("Usage v1: python3 MLdriver.py <file_name> ")
        print(
            "Usage v2: python3 MLdriver.py <file_name> <ITER_INCREASE_STEPS_LOG = 0 default>"
        )
        sys.exit(-1)
    path = sys.argv[1]

    ITER_INCREASE_STEPS_LOG = DEFAULT_ITER_INCREASE_STEPS_LOG
    ITER_INCREASE_STEPS = DEFAULT_ITER_INCREASE_STEPS
    range_ = DEFAULT_RANGE_

    if len(sys.argv) == 3 and sys.argv[2]:
        ITER_INCREASE_STEPS_LOG = int(sys.argv[2])
        ITER_INCREASE_STEPS = np.power(10, ITER_INCREASE_STEPS_LOG)
        range_ = range(ITER_INCREASE_STEPS)

    for counter in range_:
        output_name = OUTPUT_PREFIX + str(counter).zfill(
            ITER_INCREASE_STEPS_LOG)
        LinearRegressionTraining(
            path=path,
            alpha=ALPHA,
            n_iterations=int(MAX_ITER / ITER_INCREASE_STEPS * counter + 1),
            output_name=output_name,
            feature_type=POLYNOMIAL_FEATURE_TYPE,
            feature_val=3,
        )
