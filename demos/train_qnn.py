from qadence import RX, FeatureParameter, QuantumCircuit, Z, chain, hea
from qadence_model.constructors import QNN 
from perceptrain import Trainer, TrainConfig

import torch
from torch.optim import Adam
from torch.utils.data import DataLoader, TensorDataset

# Model
n_qubits = 2
features = [FeatureParameter(f"x_{i}") for i in range(n_qubits)]
feature_map = chain(*(RX(i, features[i]) for i in range(n_qubits)))
ansatz = hea(n_qubits=n_qubits, depth=1)
circuit = QuantumCircuit(n_qubits, chain(feature_map, ansatz))
observable = Z(0)
qnn = QNN(
    circuit=circuit,
    observable=observable,
    inputs=[f"x_{i}" for i in range(n_qubits)],
)

# Data & Optimizer
x = torch.linspace(0, 1, 100).reshape(-1, 2)
y = torch.cos(x[:, 0] * 3.14) + torch.sin(x[:, 1] * 3.14)
y = y.unsqueeze(1)  
dataset = TensorDataset(x, y)
dataloader = DataLoader(dataset, batch_size=10, shuffle=True)
optimizer = Adam(qnn.parameters(), lr=0.05)

# Training
if __name__ == "__main__":
    config = TrainConfig(max_iter=100, print_every=5)
    trainer = Trainer(model=qnn, optimizer=optimizer, config=config)
    result = trainer.fit(dataloader)

    print("\n")
    print("Model ----- ")
    print(result[0])