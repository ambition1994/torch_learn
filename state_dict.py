import torch
import torch.nn as nn
import torch.optim as optim
import torch.nn.functional as F


class Net(nn.Module):

    def __init__(self):
        super(Net, self).__init__()
        self.conv1 = nn.Conv2d(3, 6, 5)
        self.pool = nn.MaxPool2d(2, 2)
        self.conv2 = nn.Conv2d(6, 16, 5)
        # why 16 * 5 * 5
        self.fc1 = nn.Linear(16 * 5 * 5, 120)
        self.fc2 = nn.Linear(120, 84)
        self.fc3 = nn.Linear(84, 10)

    def forward(self, x):
        x = self.pool(F.relu(self.conv1(x)))
        x = self.pool(F.relu(self.conv2(x)))
        x = x.view(-1, 16 * 5 * 5)
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = self.fc3(x)
        return x


def main():

    net = Net()
    # print(net)

    optimizer = optim.SGD(net.parameters(), lr=0.001, momentum=0.9)

    # print model's state dict
    # print("Model's state_dict:")
    # for param_tensor in net.state_dict():
    #     print(param_tensor, "\t", net.state_dict()[param_tensor].size())
    #     print(type(net.state_dict()))

    # print()

    # print optimizer's state_dict
    # print("optimizer's state_dict:")
    # for var_name in optimizer.state_dict():
    #     print(var_name, "\t", optimizer.state_dict()[var_name])

    # *************** save our model using just state_dict *****************************
    PATH = "./model/state_dict_model.pt"

    # save
    torch.save(net.state_dict(), PATH)

    # load
    model = Net()
    model.load_state_dict(torch.load(PATH))
    # model.eval()
    print(model)

    # *************** save and load entire model *****************************
    PATH = "./model/entire_model.pt"

    # save
    torch.save(net, PATH)

    # load
    model = torch.load(PATH)
    model.eval()
    print(model)


if __name__ == "__main__":
    main()
