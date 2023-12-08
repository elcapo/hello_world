import numpy as np
from tensorflow import keras

class LinearRegressionModel():
    def __init__(self, xs, ys, epochs=500):
        self.xs = np.array(xs, dtype=float)
        self.ys = np.array(ys, dtype=float)
        self.epochs = epochs

        self.model = keras.Sequential([
            keras.layers.Dense(units=1, input_shape=[1]),
        ])

        self.model.compile(optimizer='sgd', loss='mean_squared_error')

        self.model.fit(self.xs, self.ys, epochs=self.epochs)

class TwoHiddenLayerModel():
    def __init__(self, xs, ys, epochs=500, hidden_units=4):
        self.xs = np.array(xs, dtype=float)
        self.ys = np.array(ys, dtype=float)
        self.epochs = epochs
        self.hidden_units = hidden_units

        self.model = keras.Sequential([
            keras.layers.InputLayer(input_shape=[1]),
            keras.layers.Dense(units=self.hidden_units, activation='relu'),
            keras.layers.Dense(units=self.hidden_units, activation='relu'),
            keras.layers.Dense(units=1)
        ])

        self.model.compile(optimizer='adam', loss='mean_squared_error')

        self.model.fit(self.xs, self.ys, epochs=self.epochs)