import numpy as np

from rafComputing.ML.features.feature_types import (
    POLYNOMIAL_FEATURE_TYPE,
    NO_FEATURE_TYPE,
    POWER_FEATURE_TYPE,
)


def extract_features(X=None,
                     feature_type=POLYNOMIAL_FEATURE_TYPE,
                     feature_val=1.0):
    if X is None:
        return None
    if feature_type == POLYNOMIAL_FEATURE_TYPE:
        return extract_polynomial_features(X, feature_val)
    if feature_type == POWER_FEATURE_TYPE:
        return extract_power_features(X, feature_val)
    if feature_type == NO_FEATURE_TYPE:
        return same_features(X, feature_val)


def extract_polynomial_features(X, M):
    M = int(M)
    phi = np.ones((X.size, M + 1))
    for i in range(X.size):
        for j in range(M + 1):
            phi[i][j] = np.power(X[i], j)
    return phi


def extract_power_features(X, M):
    phi = np.ones((X.size, 1))
    for i in range(X.size):
        phi[i][0] = np.power(X[i], M)
    return phi


def same_features(X, _M):
    return X
