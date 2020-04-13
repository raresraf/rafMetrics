import numpy as np
from sklearn.model_selection import train_test_split

from rafComputing.ML.features.feature_transformation import extract_features
from rafComputing.ML.features.feature_types import POLYNOMIAL_FEATURE_TYPE


def matrix_to_train_test(path,
                         feature_type=POLYNOMIAL_FEATURE_TYPE,
                         feature_val=1):
    """
        Loads a multiple-column space-separated matrix from @path,
        containing:
        Column 0: Metric key(e.g. input size)
        Column 1: Metric value(e.g. time)
        Returns as follows:
        Pair containing [ALL] extracted features and original read features (x, orig_x),
        Labels [ALL] y,
        Pair containing [Training] extracted features and original read features (X_train, orig_x_train),
        Pair containing [Test] extracted features and original read features (X_test, orig_x_test),
        Labels [Training] y_train,
        Labels [Test] y_test
    """
    matrix = np.loadtxt(path, usecols=range(2))

    # Parse Column 0: Metric key
    x = matrix[:, 0]
    # Parse Column 1: Metric value
    y = matrix[:, 1]

    # Ignore columns 2..
    x = x.reshape(-1, 1)
    y = y.reshape(-1, 1)

    # Store values for X before extract_features
    orig_x = x
    orig_x_train, orig_x_test, y_train, y_test = train_test_split(
        x, y, test_size=0.2, random_state=44)

    # Extract polynomial features
    x = extract_features(x, feature_type, feature_val)
    X_train = extract_features(orig_x_train, feature_type, feature_val)
    X_test = extract_features(orig_x_test, feature_type, feature_val)

    return (
        (x, orig_x),
        y,
        (X_train, orig_x_train),
        (X_test, orig_x_test),
        y_train,
        y_test,
    )
