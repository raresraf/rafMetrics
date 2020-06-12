import matplotlib.pyplot as plt
import numpy as np
import sys

from rafComputing.ML.CustomSettings.settings import (
    MAX_ITER,
    DEFAULT_ITER_INCREASE_STEPS_LOG,
    DEFAULT_ITER_INCREASE_STEPS,
    DEFAULT_RANGE_,
    MAX_ITER_LinearRegressionTraining,
    ALPHA_LinearRegressionTraining,
    OUTPUT_PREFIX,
    OUTPUT_PREFIX_0,
)
from rafComputing.ML.RegressionEngine.LinearRegressionGD import LinearRegressionGD
from rafComputing.ML.features.feature_transformation import extract_features
from rafComputing.ML.features.feature_types import (NO_FEATURE_TYPE,
                                                    POWER_FEATURE_TYPE)
from rafComputing.ML.helpers.load_data import matrix_to_train_test


def LinearRegressionTraining(
    path,
    alpha=ALPHA_LinearRegressionTraining,
    n_iterations=MAX_ITER_LinearRegressionTraining,
    output_name=OUTPUT_PREFIX_0,
    feature_type=NO_FEATURE_TYPE,
    feature_val=1.0,
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

    print(regression_model.w_)

    # Add additional generated data
    support_x = np.linspace(0, np.max(orig_x), 100)
    features_support_x = extract_features(support_x, feature_type, feature_val)
    support_y_predicted = regression_model.predict(features_support_x)

    # Predict
    y_predicted = regression_model.predict(x)
    y_predicted_train = regression_model.predict(x)
    y_predicted_test = regression_model.predict(x)

    orig_y_train = y_train.flatten()
    orig_y_test = y_test.flatten()

    # Data points
    plt.scatter(np.concatenate([orig_x_train, orig_x_test]),
                np.concatenate([orig_y_train, orig_y_test]),
                s=20,
                color="b")
    plt.xlabel("Input size")
    plt.ylabel("Memory (Gb)")

    # Plotting predicted values
    orig_x = orig_x.flatten()

    # Predicted values
    y_predicted = y_predicted.flatten()
    plt.plot(support_x, support_y_predicted, color="g")
    plt.legend(["Regression line", "Datapoint"])

    plt.title(
        "Memory usage: Naive Matrix Multiplication. \nComplexity function = n^2"
    )

    # Return figure
    plt.savefig(output_name)

    plt.close()


if __name__ == "__main__":
    if len(sys.argv) <= 1:
        print("Usage v1: python3 MLdriver_n3_memory.py <file_name> ")

        print(
            "python3 rafComputing/ML/snippets/demo/strassen/MLdriver_n3_memory.py rComplexity/samples/matrix_multiplication/results/sprmcrogpu-wn13/result_mem_n3_20200417113226"
        )

        sys.exit(-1)
    path = sys.argv[1]

    ITER_INCREASE_STEPS_LOG = DEFAULT_ITER_INCREASE_STEPS_LOG
    ITER_INCREASE_STEPS = DEFAULT_ITER_INCREASE_STEPS
    range_ = DEFAULT_RANGE_

    for counter in range_:
        output_name = OUTPUT_PREFIX + str(counter).zfill(
            ITER_INCREASE_STEPS_LOG)
        LinearRegressionTraining(
            path=path,
            alpha=1e-13,
            n_iterations=int(MAX_ITER / ITER_INCREASE_STEPS * counter + 1),
            output_name=output_name,
            feature_type=POWER_FEATURE_TYPE,
            feature_val=2,
        )
