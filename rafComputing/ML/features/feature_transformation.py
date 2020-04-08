import numpy as np

from rafComputing.ML.features.feature_types import POLYNOMIAL_FEATURE_TYPE


def extract_features(X=None,
                     feature_type=POLYNOMIAL_FEATURE_TYPE,
                     feature_val=1):
    if X is None:
        return None
    if feature_type == POLYNOMIAL_FEATURE_TYPE:
        return extract_polynomial_features(X, feature_val)


def extract_polynomial_features(X, M):
    phi = np.ones((X.size, M + 1))
    for i in range(X.size):
        for j in range(M + 1):
            phi[i][j] = np.power(X[i], j)
    return phi
