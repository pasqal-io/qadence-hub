# What is Perceptrain?

`Perceptrain` is a lightweight and flexible training framework built to simplify model training — from local CPU to multi-GPU distributed environments. It is especially suited for research and prototyping, offering modularity and plug-and-play components such as optimizers, loggers, and callbacks.

## What does Perceptrain offer?

Key Functionalities:
	• Seamless multi-GPU / multi-node training via Accelerator abstraction
	• Built-in support for both gradient-based and gradient-free optimization
	• Easy experiment tracking with TensorBoard and MLflow
	• YAML or Python-based configuration via TrainConfig
	• Customizable training loop via Trainer and callback hooks

Whether you’re developing a deep learning model or experimenting with new training techniques, `Perceptrain` helps you iterate faster and more reliably.

## How can we use it?

The detailed documentation can be (found here)[https://pasqal-io.github.io/perceptrain/latest/]. Below, we show a classification example of using `Trainer` in `Perceptrain`.

# Quantum Classification with Perceptrain

In this tutorial we will show how to use Qadence-Model and Perceptrain to solve a basic classification task using a hybrid quantum-classical model composed of a QNN and classical layers.

## Dataset

We will use the Iris dataset separated into training and testing sets.
The task is to classify iris plants presented as a multivariate dataset of 4 features into 3 labels (Iris Setosa, Iris Versicolour, or Iris Virginica).
When applying machine learning models, and particularly neural networks, it is recommended to normalize the data. As such, we use a common StandardScaler (we transform the data $x$ to $z = (x - u) / s$ where $u, s$ are respectively the mean and standard deviation of the training samples).

```python exec="on" source="material-block" session="classification"

import random

import torch
import torch.nn as nn
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from torch import Tensor
from torch.utils.data import DataLoader, Dataset

from qadence import RX, FeatureParameter, QuantumCircuit, Z, chain, hea, kron
from qadence_model.models import QNN
from perceptrain import TrainConfig, Trainer

class IrisDataset(Dataset):
    """The Iris dataset split into a training set and a test set.

    A StandardScaler is applied prior to applying models.
    """

    def __init__(self):
        X, y = load_iris(return_X_y=True)
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

        self.scaler = StandardScaler()
        self.scaler.fit(X_train)
        self.X = torch.tensor(self.scaler.transform(X_train), requires_grad=False)
        self.y = torch.tensor(y_train, requires_grad=False)

        self.X_test = torch.tensor(self.scaler.transform(X_test), requires_grad=False)
        self.y_test = torch.tensor(y_test, requires_grad=False)

    def __getitem__(self, index) -> tuple[Tensor, Tensor]:
        return self.X[index], self.y[index]

    def __len__(self) -> int:
        return len(self.y)

n_features = 4  # sepal length, sepal width, petal length, petal width
n_layers = 3
n_neurons_final_linear_layer = 3
n_epochs = 1000
lr = 1e-1
dataset = IrisDataset()

dataloader = DataLoader(dataset, batch_size=20, shuffle=True)

```


## Hybrid QNN

We set up the QNN part composed of multiple feature map layers, each followed by a variational layer.
The type of variational layer we use is the hardware-efficient-ansatz (HEA).
The output will be the expectation value with respect to a $Z$ observable on qubit $0$.
Then we add a simple linear layer serving as a classification head. This is equivalent to applying a weight matrix $W$ and bias vector $b$ to the output of the QNN denoted $o$, $l = W * o + b$. To obtain probabilities, we can apply the softmax function defined as: $p_i = \exp(l_i) / \sum_{j=1}^3 \exp(l_i)$.
Note softmax is not applied during training with the [cross-entropy loss](https://pytorch.org/docs/stable/generated/torch.nn.CrossEntropyLoss.html).

```python exec="on" source="material-block" session="classification"

feature_parameters = [FeatureParameter(f"x_{i}") for i in range(n_features)]
fm_layer = RX(0, feature_parameters[0])
for q in range(1, n_features):
    fm_layer = kron(fm_layer, RX(q, feature_parameters[q]))

ansatz_layers = [
    hea(n_qubits=n_features, depth=1, param_prefix=f"theta_{layer}")
    for layer in range(n_layers)
]
blocks = chain(fm_layer, ansatz_layers[0])
for layer in range(1, n_layers):
    blocks = chain(blocks, fm_layer, ansatz_layers[layer])

qc = QuantumCircuit(n_features, blocks)
qnn = QNN(circuit=qc, observable=Z(0), inputs=[f"x_{i}" for i in range(n_features)])
model = nn.Sequential(qnn, nn.Linear(1, n_neurons_final_linear_layer))

```

Below is a visualization of the QNN:

```python exec="on" source="material-block" html="1" session="classification"
from qadence.draw import html_string # markdown-exec: hide
print(html_string(qnn)) # markdown-exec: hide
```

## Training

Then we can set up the training part:

```python exec="on" source="material-block" session="classification"
opt = torch.optim.Adam(model.parameters(), lr=lr)
criterion = nn.CrossEntropyLoss()

def cross_entropy(model: nn.Module, data: Tensor) -> tuple[Tensor, dict]:
    x, y = data
    out = model(x)
    loss = criterion(out, y)
    return loss, {}

train_config = TrainConfig(max_iter=n_epochs, print_every=10, create_subfolder_per_run=True)
Trainer.set_use_grad(True)
trainer = Trainer(model=model, optimizer=opt, config=train_config, loss_fn=cross_entropy)


res_train = trainer.fit(dataloader)
```

## Inference

Finally, we can apply our model on the test set and check the score.

```python exec="on" source="material-block" session="classification"
X_test, y_test = dataset.X_test, dataset.y_test
preds_test = torch.argmax(torch.softmax(model(X_test), dim=1), dim=1)
accuracy_test = (preds_test == y_test).type(torch.float32).mean()
## Should reach higher than 0.9
print(f"Test Accuracy: {accuracy_test.item()}") # markdown-exec: hide
```
