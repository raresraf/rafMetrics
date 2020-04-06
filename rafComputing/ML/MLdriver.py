import sys

import matplotlib.pyplot as plt
import numpy as np
from numpy.polynomial import Polynomial as P
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split

from rafComputing.ML.MLengine import LinearRegressionUsingGD
from rafComputing.ML.polynomial_to_latex import polynomial_to_LaTeX


def matrix_to_train_test(polynomial_features):
    matrix = np.loadtxt(sys.argv[1], usecols=range(2))

    x = matrix[:, 0]
    y = matrix[:, 1]
    x = x.reshape(-1, 1)
    y = y.reshape(-1, 1)

    orig_x = x
    orig_y = y

    orig_x_train, orig_x_test, y_train, y_test = train_test_split(
        x, y, test_size=0.2, random_state=44)

    # Extract polynomial features
    x = extract_polynomial_features(x, polynomial_features)

    X_train = extract_polynomial_features(orig_x_train, polynomial_features)
    X_test = extract_polynomial_features(orig_x_test, polynomial_features)
    return (x, orig_x), y, (X_train,
                            orig_x_train), (X_test,
                                            orig_x_test), y_train, y_test


def extract_polynomial_features(X, M):
    phi = np.ones((X.size, M + 1))
    for i in range(X.size):
        for j in range(M + 1):
            phi[i][j] = np.power(X[i], j)
    return phi


def LinearRegressionTraining(alpha=.1e-20,
                             n_iterations=10000,
                             output_name="result_0"):
    (x, orig_x), y, (X_train, orig_x_train), (
        X_test, orig_x_test), y_train, y_test = matrix_to_train_test(3)

    # Model initialization
    regression_model = LinearRegressionUsingGD(alpha, n_iterations)
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

    orig_y_train = y_train.flatten()
    orig_y_test = y_test.flatten()

    # data points
    plt.scatter(orig_x_train, orig_y_train, s=20, color='b')
    plt.scatter(orig_x_test, orig_y_test, s=40, color='r')
    plt.xlabel('Input size')
    plt.ylabel('Time (seconds)')

    # plotting predicted values
    orig_x = orig_x.flatten()
    orig_y = y.flatten()

    # predicted values
    y_predicted = y_predicted.flatten()
    plt.plot(orig_x, y_predicted, color='g')
    plt.legend(['Regression line', 'Train data', 'Test data'])
    plt.title(polynomial_to_LaTeX(P(regression_model.w_.flatten())))

    # Return figure
    plt.savefig(output_name)

    plt.close()


if __name__ == "__main__":
    if len(sys.argv) <= 1:
        print("Usage: python3 MLdriver.py <file_name> ")
        print(
            "Usage: python3 MLdriver.py <file_name> <ITER_INCREASE_STEPS_LOG = 0 default>"
        )
        sys.exit(-1)

    MAX_ITER = 10000

    if len(sys.argv) == 3 and sys.argv[2]:
        ITER_INCREASE_STEPS_LOG = int(sys.argv[2])
        ITER_INCREASE_STEPS = np.power(10, ITER_INCREASE_STEPS_LOG)
        range_ = range(ITER_INCREASE_STEPS)
    else:
        ITER_INCREASE_STEPS_LOG = 0
        ITER_INCREASE_STEPS = 1
        range_ = range(1, 2)

    for counter in range_:
        output_name = 'result_' + str(counter).zfill(ITER_INCREASE_STEPS_LOG)
        LinearRegressionTraining(
            alpha=1e-25,
            n_iterations=int(MAX_ITER / ITER_INCREASE_STEPS * counter + 1),
            output_name=output_name)