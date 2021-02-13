import os
from constants import PARENT
import tensorflow as tf
import numpy as np


if not os.path.isfile(os.path.join(PARENT, "model.h5")):
    data = tf.keras.datasets.mnist
    (training_data, training_labels), (test_data, test_labels) = data.load_data()

    model = tf.keras.models.Sequential([
        tf.keras.layers.Flatten(input_shape=(28, 28)),
        tf.keras.layers.Dense(128, activation='relu'),
        tf.keras.layers.Dropout(0.2),
        tf.keras.layers.Dense(10)
    ])


    model.compile("adam", tf.keras.losses.SparseCategoricalCrossentropy(True), ["accuracy"])

    model.fit(training_data, training_labels, 10, 5)

    model.save("model.h5")

else:
    model = tf.keras.models.load_model(os.path.join(PARENT, "model.h5"))


def get_num(values):
    if np.sum(values) > 0:
        prediction = model.predict(values)
        return np.argmax(prediction)
    else:
        return "None"
