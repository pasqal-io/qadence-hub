In `qadence-model`, the `QNN` is a variational quantum model that can potentially take multi-dimensional input.

The `QNN` class needs a circuit and a list of observables; the number of feature parameters in the input circuit determines the number of input features (i.e. the dimensionality of the classical data given as input) whereas the number of observables determines the number of outputs of the quantum neural network.

The circuit has two parts, the feature map and the ansatz. The feature map is responsible for encoding the input data into the quantum state, while the ansatz is responsible for the variational part of the model. In addition, a third part of the QNN is the observables, which is (a list of) operators that are measured at the end of the circuit. In this tutorial, we will see how to do the same using configs.

One convenient way to construct these two parts of the model is to use the config classes, namely, `FeatureMapConfig` and `AnsatzConfig`. These classes allow you to specify the type of circuit and the parameters of the circuit in a structured way.

## Defining the Observable

The model output is the expectation value of the defined observable(s). We use the `ObservableConfig` class to specify the observable.

It can be used to create Hamiltonians with 2-qubit interactions and single-qubit detunings. Any Hamiltonian supported by `hamiltonian_factory` can be specified as an observable.
For example, suppose we want to measure the Z operator:

```python exec="on" source="material-block" session="config" html="1"
from qadence import ObservableConfig, Z
from qadence_model.models import create_observable
from qadence.draw import html_string # markdown-exec: hide

observable_config = ObservableConfig(
    detuning=Z,
    interaction = None,
    scale = 2.0,
    shift=-1.0,
)

observable = create_observable(register=4, config=observable_config)

print(html_string(observable)) # markdown-exec: hide
```

## Defining the Feature Map

Let us say we want to build a 4-qubit QNN that takes two inputs, namely, the $x$ and the $y$ coordinates of a point in the plane. We can use the `FeatureMapConfig` class to specify the feature map.

```python exec="on" source="material-block" session="config" html="1"
from qadence import BasisSet, chain, ReuploadScaling
from qadence_model.models import create_fm_blocks, FeatureMapConfig
from qadence.draw import html_string # markdown-exec: hide

fm_config = FeatureMapConfig(
    num_features=2,
    inputs = ["x", "y"],
    basis_set=BasisSet.CHEBYSHEV,
    reupload_scaling=ReuploadScaling.TOWER,
    feature_range={
        "x": (-1.0, 1.0),
        "y": (0.0, 1.0),
    },
)

fm_blocks = create_fm_blocks(register=4, config=fm_config)
feature_map = chain(*fm_blocks)
print(html_string(feature_map)) # markdown-exec: hide
```

We have specified that the feature map should take two features, and have named the `FeatureParameter` "x" and "y" respectively. Both these parameters are encoded using the Chebyshev basis set, and the reupload scaling is set to `ReuploadScaling.TOWER`. One can optionally add the basis and the reupload scaling for each parameter separately.

The `feature_range` parameter is a dictionary that specifies the range of values that each feature comes from. This is useful for scaling the input data to the range that the encoding function can handle. In default case, this range is mapped to the target range of the Chebyshev basis set which is $[-1, 1]$. One can also specify the target range for each feature separately..

## Defining the Ansatz

The next part of the QNN is the ansatz. We use `AnsatzConfig` class to specify the type of ansatz.

Let us say, we want to follow this feature map with 2 layers of hardware efficient ansatz.

```python exec="on" source="material-block" session="config" html="1"
from qadence import AnsatzType, Strategy
from qadence_model.models import AnsatzConfig, create_ansatz
from qadence.draw import html_string # markdown-exec: hide

ansatz_config = AnsatzConfig(
    depth=2,
    ansatz_type=AnsatzType.HEA,
    ansatz_strategy=Strategy.DIGITAL,
)

ansatz = create_ansatz(register=4, config=ansatz_config)

print(html_string(ansatz)) # markdown-exec: hide
```

We have specified that the ansatz should have a depth of 2, and the ansatz type is "hea" (Hardware Efficient Ansatz). The ansatz strategy is set to "digital", which means digital gates are being used. One could alternatively use "analog" or "rydberg" as the ansatz strategy.

## Defining the QNN from the Configs

To build the QNN, we can now use the `QNN` class as a `QuantumModel` subtype. In addition to the feature map, ansatz and the observable configs, we can also specify options such as the `backend`, `diff_mode`, etc.

```python exec="on" source="material-block" session="config" html="1"
from qadence import BackendName, DiffMode, ObservableConfig, Z
from qadence_model.models import QNN
from qadence.draw import html_string # markdown-exec: hide

observable_config = ObservableConfig(
    detuning=Z,
    interaction = None,
    scale = 2.0,
    shift=-1.0,
)

qnn = QNN.from_configs(
    register=4,
    obs_config=observable_config,
    fm_config=fm_config,
    ansatz_config=ansatz_config,
    backend=BackendName.PYQTORCH,
    diff_mode=DiffMode.AD,
)

print(html_string(qnn)) # markdown-exec: hide
```
