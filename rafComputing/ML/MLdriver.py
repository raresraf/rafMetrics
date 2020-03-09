import numpy as np
import matplotlib.pyplot as plt
import sys

# from sklearn.metrics import mean_squared_error, r2_score

from rafComputing.ML.MLengine import LinearRegressionUsingGD


def extract_polynomial_features(X, M):
    phi = np.ones((X.size, M + 1))
    for i in range(X.size):
        for j in range(M + 1):
            phi[i][j] = np.power(X[i], j)
    return phi


if __name__ == "__main__":
    if len(sys.argv) <= 1:
        print("Usage: python3 MLdriver.py <file_name>")
        sys.exit(-1)

    matrix = np.loadtxt(sys.argv[1], usecols=range(2))

    x = matrix[:, 0]
    y = matrix[:, 1]
    x = x.reshape(-1, 1)
    y = y.reshape(-1, 1)

    orig_x = x
    x = extract_polynomial_features(x, 3)

    # Model initialization
    regression_model = LinearRegressionUsingGD()

    # Fit the data(train the model)
    regression_model.fit(x, y)

    # Predict
    y_predicted = regression_model.predict(x)

    # model evaluation
    # rmse = mean_squared_error(y, y_predicted)
    # r2 = r2_score(y, y_predicted)

    # printing values
    print('Slope:', regression_model.w_[0][0])
    # print('Intercept:', regression_model.intercept_)
    # print('Root mean squared error: ', rmse)
    # print('R2 score: ', r2)

    # plotting values

    orig_x = orig_x.flatten()
    orig_y = y.flatten()

    # data points
    plt.scatter(orig_x, orig_y, s=10)
    plt.xlabel('x')
    plt.ylabel('y')

    y_predicted = y_predicted.flatten()
    # predicted values
    plt.plot(orig_x, y_predicted, color='r')
    plt.show()
