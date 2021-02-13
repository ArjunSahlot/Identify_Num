import os
from constants import PARENT
import tensorflow as tf
import numpy as np


if not os.path.isfile(os.path.join(PARENT, "model.h5")):
    mnist = tf.keras.datasets.mnist
    (x_train, y_train), (x_test, y_test) = mnist.load_data()
    x_train, x_test = x_train / 255.0, x_test / 255.0

    model = tf.keras.models.Sequential([
        tf.keras.layers.Flatten(input_shape=(28, 28)),
        tf.keras.layers.Dense(128, activation='relu'),
        tf.keras.layers.Dropout(0.2),
        tf.keras.layers.Dense(10)
    ])


    model.compile("adam", tf.keras.losses.SparseCategoricalCrossentropy(True), ["accuracy"])

    model.fit(x_train, y_train, epochs=5)

    model.save("model.h5")

else:
    model = tf.keras.models.load_model(os.path.join(PARENT, "model.h5"))


def get_num(values):
    if np.sum(values) > 0:
        print(tf.nn.softmax(model.predict(values)))
        prediction = model.predict(values)
        return np.argmax(prediction)
    else:
        return "None"
