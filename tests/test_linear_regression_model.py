import numpy as np
from hello_world.linear_regression_model import LinearRegressionModel

def test_predict():
    xs = [-1.0, 0.0, 1.0, 2.0, 3.0, 4.0]
    ys = [-3.0, -1.0, 1.0, 3.0, 5.0, 7.0]
    model = LinearRegressionModel(xs, ys)
    assert(np.isclose(model.predict([10.0]), 19.00, 0.01))