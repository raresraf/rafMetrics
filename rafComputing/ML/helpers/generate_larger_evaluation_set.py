import numpy as np

DISCOUNT_FACTOR = 16


def generate_larger_evaluation_set(x):
    PREDICTION_RANGE = int(np.size(x) / DISCOUNT_FACTOR)

    latest_element = np.max(x)
    latest_element2 = np.partition(x.flatten(), -2)[-2]
    diff = DISCOUNT_FACTOR * (latest_element - latest_element2)

    extra_x = np.array([])
    for it in range(0, PREDICTION_RANGE + 1):
        extra_x = np.append(extra_x, latest_element + diff * it)

    return extra_x
