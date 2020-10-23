import os
import torch
import torchvision
from torchvision import transforms, datasets
import torch.optim as optim
from Identify_Num.ml.network import Network
from Identify_Num.constants import PARENT
import torch.nn.functional as F
import tensorflow as tf
import numpy as np


arg = input("What library do you want to use (tensorflow/pytorch): ").lower()
pytorch = "torch" in arg or "p" in arg or "y" in arg

if pytorch:
    if not os.path.isfile(os.path.join(PARENT, "ml", "network.model")):
        train = datasets.MNIST(os.path.join(PARENT, "ml"), train=True, download=True,
                               transform=transforms.Compose([
                                   transforms.ToTensor()
                               ]))

        test = datasets.MNIST(os.path.join(PARENT, "ml"), train=False, download=True,
                              transform=transforms.Compose([
                                  transforms.ToTensor()
                              ]))

        trainset = torch.utils.data.DataLoader(train, batch_size=10, shuffle=True)
        testset = torch.utils.data.DataLoader(test, batch_size=10, shuffle=False)

        net = Network()

        optimizer = optim.Adam(net.parameters())

        for epoch in range(3):
            for data in trainset:
                X, y = data
                net.zero_grad()
                output = net(X.view(-1, 28 ** 2))
                loss = F.nll_loss(output, y)
                loss.backward()
                optimizer.step()

        correct = 0
        total = 0

        with torch.no_grad():
            for data in testset:
                X, y = data
                output = net(X.view(-1, 28 ** 2))
                for idx, i in enumerate(output):
                    if torch.argmax(i) == y[idx]:
                        correct += 1
                    total += 1

        print("Accuracy:", round(correct / total, 3))
        net.save()

    else:
        net = Network()
        net.load_state_dict(torch.load(os.path.join(PARENT, "ml", "network.model")))
        net.eval()

else:
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
