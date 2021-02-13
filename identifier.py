import os
from constants import PARENT
import tensorflow as tf
import numpy as np


arg = input("What library do you want to use (tensorflow/pytorch): ").lower()
pytorch = "torch" in arg or "p" in arg or "y" in arg

if not os.path.isfile(os.path.join(PARENT, "ml", "model.h5")):
    data = tf.keras.datasets.mnist
    (training_data, training_labels), (test_data, test_labels) = data.load_data()

    model = tf.keras.Sequential([
        tf.keras.layers.Flatten(input_shape=(28, 28)),
        tf.keras.layers.Dense(128, activation=tf.nn.relu),
        tf.keras.layers.Dense(128, activation=tf.nn.relu),
        tf.keras.layers.Dense(10, activation=tf.nn.softmax)
    ])

    model.compile(tf.optimizers.Adam(), "sparse_categorical_crossentropy", metrics=["accuracy"])

    model.fit(training_data, training_labels, 10, 5)

    model.save("model.h5")

else:
    model = tf.keras.models.load_model(os.path.join(PARENT, "ml", "model.h5"))


def get_num(values):
    if pytorch:
        try:
            return torch.argmax(net(values.view(-1, 28**2))[0])
        except TypeError:
            return "None"
    else:
        if np.sum(values) > 0:
            prediction = model.predict(values)
            return np.argmax(prediction)
        else:
            return "None"


def get_mode():
    return pytorch
