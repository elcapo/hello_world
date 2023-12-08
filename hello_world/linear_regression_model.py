import numpy as np
from tensorflow import keras

class LinearRegressionModel():
    def __init__(self, xs, ys, epochs=500):
        self.model = keras.Sequential([
            keras.layers.Dense(units=1, input_shape=[1])
        ])

        self.model.compile(optimizer='sgd', loss='mean_squared_error')

        self.xs = np.array(xs, dtype=float)
        self.ys = np.array(ys, dtype=float)
        self.epochs = epochs

        self.model.fit(self.xs, self.ys, epochs=self.epochs)

    def predict(self, qs):
        return self.model.predict([qs])
