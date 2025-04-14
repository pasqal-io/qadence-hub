# from __future__ import annotations

# import pytest
# import torch

# from qadence_model.models import QNN
# from perceptrain import DictDataLoader, TrainConfig, Trainer, to_dataloader
# from conftest_model import *


# @pytest.mark.flaky(max_runs=10)
# def test_fit_sin_adjoint(BasicAdjointQNN: torch.nn.Module) -> None:
#     model = BasicAdjointQNN
#     batch_size = 5
#     n_epochs = 200
#     criterion = torch.nn.MSELoss()
#     optimizer = torch.optim.Adam(model.parameters(), lr=0.1)

#     for _ in range(n_epochs):
#         optimizer.zero_grad()
#         x_train = torch.rand(batch_size, 1)
#         y_train = torch.sin(x_train)
#         out = model(x_train)
#         loss = criterion(out, y_train)
#         loss.backward()
#         optimizer.step()

#     x_test = torch.rand(1, 1)
#     assert torch.allclose(torch.sin(x_test), model(x_test), rtol=1e-1, atol=1e-1)
