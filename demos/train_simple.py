import torch
import torch.nn as nn
from torch.utils.data import DataLoader, TensorDataset

from perceptrain import Trainer, TrainConfig
from torch.optim import SGD

# Model
class SimpleModel(nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = nn.Linear(1, 1)
    def forward(self, x):
        return self.linear(x)
X = torch.tensor([[1.0], [2.0], [3.0], [4.0]])
y = torch.tensor([[2.0], [4.0], [6.0], [8.0]])
model = SimpleModel()

# Data and Optimizer
dataset = TensorDataset(X, y)
dataloader = DataLoader(dataset, batch_size=2)
optimizer = SGD(model.parameters(), lr=0.01)


# Training
if __name__ == "__main__":
    config = TrainConfig(max_iter=100, print_every=5)
    trainer = Trainer(model=model, optimizer=optimizer, config=config)
    result = trainer.fit(dataloader)

    print("\n")
    print("Model ----- ")
    print(result[0])