import torch
from torch import nn
from torch.utils.data import DataLoader, TensorDataset
from perceptrain.train_utils import Accelerator


def train_fn(epochs, model, dataloader, optimizer, accelerator):
    # Acc - prepare to prepare the models/data/optimizer for distribution 
    model, optimizer, dataloader = accelerator.prepare(model, optimizer, dataloader)

    model.train()
    for epoch in range(epochs):
        for batch in dataloader:

            # Acc - Prepare the batch of data
            batch = accelerator.prepare_batch(batch)
            x, y = batch

            optimizer.zero_grad()
            preds = model(x)
            loss = torch.nn.functional.mse_loss(preds, y)
            loss.backward()
            optimizer.step()

        # if accelerator.rank == 0:
        print(f"Rank {accelerator.rank} | Epoch {epoch} | Loss: {loss.item():.4f}")


if __name__ == "__main__":
    # Model: y = Wx + b
    model = nn.Linear(1, 1)
    optimizer = torch.optim.SGD(model.parameters(), lr=0.1)
    x = torch.linspace(0, 1, 100).reshape(-1, 1)
    y = 2 * x
    dataset = TensorDataset(x, y)
    dataloader = DataLoader(dataset, batch_size=10, shuffle=True)

    accelerator = Accelerator(
        nprocs=5,                # 2 processes
        compute_setup="cpu",     # Use CPU
        backend="gloo"           # GLOO backend for CPU
    )

    # Run distributed training
    distributed_train = accelerator.distribute(train_fn)
    distributed_train(epochs=5, model=model, dataloader=dataloader, optimizer=optimizer, accelerator=accelerator)
