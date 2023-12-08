import numpy as np
from hello_world.models import LinearRegressionModel

def test_predict():
    xs = [-1.0, 0.0, 1.0, 2.0, 3.0, 4.0]
    ys = [-3.0, -1.0, 1.0, 3.0, 5.0, 7.0]
    linear_regression = LinearRegressionModel(xs, ys)
    assert(np.isclose(linear_regression.model.predict([10.0]), 19.00, 0.01))
