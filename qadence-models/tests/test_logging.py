# from __future__ import annotations

# from pathlib import Path
# from itertools import count

# import torch
# from torch.optim import Optimizer
# from torch.utils.data import DataLoader

# from perceptrain import TrainConfig, Trainer
# from qadence_models.models import QNN
# from qadence.model import QuantumModel
# from qadence.types import ExperimentTrackingTool
# from qadence_models.utils import rand_featureparameters

# from perceptrain.data import to_dataloader


# def dataloader(batch_size: int = 25) -> DataLoader:
#     x = torch.linspace(0, 1, batch_size).reshape(-1, 1)
#     y = torch.cos(x)
#     return to_dataloader(x, y, batch_size=batch_size, infinite=True)


# def setup_model(model: Module) -> tuple[Callable, Optimizer]:
#     cnt = count()
#     criterion = torch.nn.MSELoss()
#     optimizer = torch.optim.Adam(model.parameters(), lr=0.1)
#     inputs = rand_featureparameters(model, 1)

#     def loss_fn(model: QuantumModel, data: torch.Tensor) -> tuple[torch.Tensor, dict]:
#         next(cnt)
#         out = model.expectation(inputs)
#         loss = criterion(out, torch.rand(1))
#         return loss, {}

#     return loss_fn, optimizer


# # def test_model_logging_mlflow_basicQM(BasicQuantumModel: QuantumModel, tmp_path: Path) -> None:
# #     model = BasicQuantumModel
# #     loss_fn, optimizer = setup_model(model)

# #     config = TrainConfig(
# #         root_folder=tmp_path,
# #         max_iter=10,  # type: ignore
# #         checkpoint_every=1,
# #         write_every=1,
# #         log_model=True,
# #         tracking_tool=ExperimentTrackingTool.MLFLOW,
# #     )

# #     trainer = Trainer(model, optimizer, config, loss_fn, None)
# #     with trainer.enable_grad_opt():
# #         trainer.fit()

# #     load_mlflow_model(trainer.callback_manager.writer)

# #     clean_mlflow_experiment(trainer.callback_manager.writer)


# # def test_model_logging_mlflow_basicQNN(BasicQNN: QNN, tmp_path: Path) -> None:
# #     data = dataloader()
# #     model = BasicQNN

# #     loss_fn, optimizer = setup_model(model)

# #     config = TrainConfig(
# #         root_folder=tmp_path,
# #         max_iter=10,  # type: ignore
# #         checkpoint_every=1,
# #         write_every=1,
# #         log_model=True,
# #         tracking_tool=ExperimentTrackingTool.MLFLOW,
# #     )

# #     trainer = Trainer(model, optimizer, config, loss_fn, data)
# #     with trainer.enable_grad_opt():
# #         trainer.fit()

# #     load_mlflow_model(trainer.callback_manager.writer)

# #     clean_mlflow_experiment(trainer.callback_manager.writer)


# # def test_model_logging_mlflow_basicAdjQNN(BasicAdjointQNN: QNN, tmp_path: Path) -> None:
# #     data = dataloader()
# #     model = BasicAdjointQNN

# #     loss_fn, optimizer = setup_model(model)

# #     config = TrainConfig(
# #         root_folder=tmp_path,
# #         max_iter=10,  # type: ignore
# #         checkpoint_every=1,
# #         write_every=1,
# #         log_model=True,
# #         tracking_tool=ExperimentTrackingTool.MLFLOW,
# #     )

# #     trainer = Trainer(model, optimizer, config, loss_fn, data)
# #     with trainer.enable_grad_opt():
# #         trainer.fit()

# #     load_mlflow_model(trainer.callback_manager.writer)

# #     clean_mlflow_experiment(trainer.callback_manager.writer)
