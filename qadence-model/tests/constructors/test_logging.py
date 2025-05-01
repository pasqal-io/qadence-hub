from __future__ import annotations

import os
import shutil
from pathlib import Path
from itertools import count
from urllib.parse import urlparse
from typing import Callable


import torch
from torch.optim import Optimizer
from torch.utils.data import DataLoader
from torch.nn import Module


import mlflow
from mlflow import MlflowClient
from mlflow.entities import Run

from qadence.types import ExperimentTrackingTool
from qadence_model.constructors.qnn_model import QNN
from qadence.model import QuantumModel
from qadence_model.constructors.qnn_utils import rand_featureparameters

from perceptrain import TrainConfig, Trainer
from perceptrain.callbacks.writer_registry import BaseWriter
from perceptrain.data import to_dataloader


def dataloader(batch_size: int = 25) -> DataLoader:
    x = torch.linspace(0, 1, batch_size).reshape(-1, 1)
    y = torch.cos(x)
    return to_dataloader(x, y, batch_size=batch_size, infinite=True)


def setup_model(model: Module) -> tuple[Callable, Optimizer]:
    cnt = count()
    criterion = torch.nn.MSELoss()
    optimizer = torch.optim.Adam(model.parameters(), lr=0.1)
    inputs = rand_featureparameters(model, 1)

    def loss_fn(model: QuantumModel, data: torch.Tensor) -> tuple[torch.Tensor, dict]:
        next(cnt)
        out = model.expectation(inputs)
        loss = criterion(out, torch.rand(1))
        return loss, {}

    return loss_fn, optimizer


def load_mlflow_model(writer: BaseWriter) -> None:
    run_id = writer.run.info.run_id

    mlflow.pytorch.load_model(model_uri=f"runs:/{run_id}/model")


def find_mlflow_artifacts_path(run: Run) -> Path:
    artifact_uri = run.info.artifact_uri
    parsed_uri = urlparse(artifact_uri)
    return Path(os.path.abspath(os.path.join(parsed_uri.netloc, parsed_uri.path)))


def clean_mlflow_experiment(writer: BaseWriter) -> None:
    experiment_id = writer.run.info.experiment_id
    client = MlflowClient()

    runs = client.search_runs(experiment_id)

    def clean_artifacts(run: Run) -> None:
        local_path = find_mlflow_artifacts_path(run)
        shutil.rmtree(local_path)

    for run in runs:
        clean_artifacts(run)

        run_id = run.info.run_id
        client.delete_run(run_id)

        mlruns_base_dir = "./mlruns"
        if os.path.isdir(mlruns_base_dir):
            shutil.rmtree(os.path.join(mlruns_base_dir, experiment_id))


def test_model_logging_mlflow_basicQM(BasicQuantumModel: QuantumModel, tmp_path: Path) -> None:
    model = BasicQuantumModel
    loss_fn, optimizer = setup_model(model)

    config = TrainConfig(
        root_folder=tmp_path,
        max_iter=10,  # type: ignore
        checkpoint_every=1,
        write_every=1,
        log_model=True,
        tracking_tool=ExperimentTrackingTool.MLFLOW,
    )

    trainer = Trainer(model, optimizer, config, loss_fn, None)
    with trainer.enable_grad_opt():
        trainer.fit()

    load_mlflow_model(trainer.callback_manager.writer)

    clean_mlflow_experiment(trainer.callback_manager.writer)


def test_model_logging_mlflow_basicQNN(BasicQNN: QNN, tmp_path: Path) -> None:
    data = dataloader()
    model = BasicQNN

    loss_fn, optimizer = setup_model(model)

    config = TrainConfig(
        root_folder=tmp_path,
        max_iter=10,  # type: ignore
        checkpoint_every=1,
        write_every=1,
        log_model=True,
        tracking_tool=ExperimentTrackingTool.MLFLOW,
    )

    trainer = Trainer(model, optimizer, config, loss_fn, data)
    with trainer.enable_grad_opt():
        trainer.fit()

    load_mlflow_model(trainer.callback_manager.writer)

    clean_mlflow_experiment(trainer.callback_manager.writer)


def test_model_logging_mlflow_basicAdjQNN(BasicAdjointQNN: QNN, tmp_path: Path) -> None:
    data = dataloader()
    model = BasicAdjointQNN

    loss_fn, optimizer = setup_model(model)

    config = TrainConfig(
        root_folder=tmp_path,
        max_iter=10,  # type: ignore
        checkpoint_every=1,
        write_every=1,
        log_model=True,
        tracking_tool=ExperimentTrackingTool.MLFLOW,
    )

    trainer = Trainer(model, optimizer, config, loss_fn, data)
    with trainer.enable_grad_opt():
        trainer.fit()

    load_mlflow_model(trainer.callback_manager.writer)

    clean_mlflow_experiment(trainer.callback_manager.writer)
