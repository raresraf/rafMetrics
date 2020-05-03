import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error, r2_score

from rafComputing.ML.CustomSettings.settings import (
    MAX_ITER_LinearRegressionTraining,
    ALPHA_LinearRegressionTraining,
    AUTO_DRIVER_DEFAULT_OUTPUT_NAME,
)
from rafComputing.ML.RegressionEngine.LinearRegressionGD import LinearRegressionGD
from rafComputing.ML.features.feature_types import (
    NO_FEATURE_TYPE, )
from rafComputing.ML.helpers.generate_larger_evaluation_set import generate_larger_evaluation_set
from rafComputing.ML.helpers.load_data import matrix_to_train_test_w_generate_larger_evaluation_set
from rafComputing.ML.snippets.MLdriver_more_graphs_prediction import TEST_POINT_COLORS, LINE_COLORS


def CustomStrassenLinearRegressionTrainingMoreGraphsPrediction(
    path,
    alpha=ALPHA_LinearRegressionTraining,
    n_iterations=MAX_ITER_LinearRegressionTraining,
    internal_counter=0,
    feature_type=NO_FEATURE_TYPE,
    feature_val=1.0,
    _first=True,
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

    # Data points
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
    plt.plot(orig_x_test2,
             y_predicted_test2,
             color=LINE_COLORS[internal_counter],
             linestyle="--")

    if final:
        plt.legend(plt_legend, fontsize=8)

        # Return figure
        plt.savefig(AUTO_DRIVER_DEFAULT_OUTPUT_NAME)
        plt.close()
