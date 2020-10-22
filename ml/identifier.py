import torch
import torchvision
from torchvision import transforms, datasets
import torch.optim as optim
from Identify_Num.ml.network import Network
import torch.nn.functional as F

train = datasets.MNIST("", train=True, download=True,
                       transform=transforms.Compose([
                           transforms.ToTensor()
                       ]))

test = datasets.MNIST("", train=False, download=True,
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


# correct = 0
# total = 0
#
# with torch.no_grad():
#     for data in trainset:
#         X, y = data
#         output = net(X.view(-1, 28**2))
#         for idx, i in enumerate(output):
#             if torch.argmax(i) == y[idx]:
#                 correct += 1
#             total += 1


def get_num(values):
    return torch.argmax(net(values.view(-1, 28**2))[0])
