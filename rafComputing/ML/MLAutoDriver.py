import numpy as np
import matplotlib.pyplot as plt
import sys

from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Ridge

from numpy.polynomial import Polynomial as P

from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split

from rafComputing.ML.MLdriver import matrix_to_train_test
from rafComputing.ML.MLengine import LinearRegressionUsingGD
from rafComputing.ML.polynomial_to_latex import polynomial_to_LaTeX

OUTPUT_NAME = 'result.png'


def LinearRegressionTrainingAuto():
    (x, orig_x), (
        y, orig_y), X_train, X_test, y_train, y_test = matrix_to_train_test(3)

    # Model initialization
    regression_model = LinearRegression(fit_intercept=False)
    regression_model.fit(X_train, y_train)

    # Predict
    y_predicted = regression_model.predict(x)
    y_predicted_train = regression_model.predict(X_train)
    y_predicted_test = regression_model.predict(X_test)

    # Model evaluation training data
    rmse = mean_squared_error(y_train, y_predicted_train)
    r2 = r2_score(y_train, y_predicted_train)
    print('[Training Set] Root mean squared error: ', rmse)
    print('[Training Set] R2 score: ', r2)

    # Model evaluation test data
    rmse = mean_squared_error(y_test, y_predicted_test)
    r2 = r2_score(y_test, y_predicted_test)
    print('[Test Set] Root mean squared error: ', rmse)
    print('[Test Set] R2 score: ', r2)

    orig_x_train = X_train[:, 1]
    orig_y_train = y_train.flatten()
    orig_x_test = X_test[:, 1]
    orig_y_test = y_test.flatten()

    # data points
    plt.scatter(orig_x_train, orig_y_train, s=20, color='b')
    plt.scatter(orig_x_test, orig_y_test, s=40, color='r')
    plt.xlabel('Input size')
    plt.ylabel('Time (seconds)')

    # plotting predicted values
    orig_x = orig_x.flatten()
    orig_y = orig_y.flatten()

    # predicted values
    y_predicted = y_predicted.flatten()
    plt.plot(orig_x, y_predicted, color='g')
    plt.legend(['Regression line', 'Train data', 'Test data'])
    plt.title(polynomial_to_LaTeX(P(regression_model.coef_.flatten())))

    # Return figure
    plt.savefig(OUTPUT_NAME)

    plt.close()


if __name__ == "__main__":
    if len(sys.argv) <= 1:
        print("Usage: python3 MLAutoDriver.py <file_name> ")
        sys.exit(-1)

    LinearRegressionTrainingAuto()
