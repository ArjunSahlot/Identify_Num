#
#  Identify num
#  An AI that can recognize the number you draw. Made using pygame and tensorflow
#  Copyright Arjun Sahlot 2021
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <https://www.gnu.org/licenses/>.
#

import os
from constants import PARENT
import tensorflow as tf
import numpy as np


if not os.path.isfile(os.path.join(PARENT, "model.h5")):
    mnist = tf.keras.datasets.mnist
    (x_train, y_train), (x_test, y_test) = mnist.load_data()
    x_train = tf.keras.utils.normalize(x_train, axis=1)
    x_test = tf.keras.utils.normalize(x_test, axis=1)

    model = tf.keras.models.Sequential([
        tf.keras.layers.Flatten(input_shape=(28, 28)),
        tf.keras.layers.Dense(128, activation=tf.nn.relu),
        tf.keras.layers.Dense(128, activation=tf.nn.relu),
        tf.keras.layers.Dense(10, activation=tf.nn.softmax)
    ])

    model.compile("adam", tf.keras.losses.SparseCategoricalCrossentropy(True), ["accuracy"])

    model.fit(x_train, y_train, epochs=5)

    model.save("model.h5")

else:
    model = tf.keras.models.load_model(os.path.join(PARENT, "model.h5"))


def get_num(values):
    if np.sum(values) > 0:
        prediction = model.predict(values)[0]
        return np.argmax(prediction)
    else:
        return "None"
