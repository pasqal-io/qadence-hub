import torch
from torch import nn
from torch.utils.data import DataLoader, TensorDataset
from torch.optim import SGD

from perceptrain import Trainer, TrainConfig
from perceptrain.types import ExperimentTrackingTool

# model
model = nn.Linear(1, 1)

# Dataset and optimizer
x = torch.linspace(0, 1, 100).reshape(-1, 1)
y = 2 * x
dataset = TensorDataset(x, y)
dataloader = DataLoader(dataset, batch_size=10, shuffle=True)
optimizer = SGD(model.parameters(), lr=0.1)

# Define training config with MLflow tracking
config = TrainConfig(
    max_iter=10,
    print_every=1,
    write_every=1,
    tracking_tool=ExperimentTrackingTool.MLFLOW,
    log_model=True,
    hyperparams={"lr": 0.1, "batch_size": 10}
)

# Trainer setup
trainer = Trainer(model=model,optimizer=optimizer,config=config)
result = trainer.fit(train_dataloader=dataloader)
