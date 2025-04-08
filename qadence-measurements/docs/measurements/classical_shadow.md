# Classical shadows

A much less resource demanding protocol based on _classical shadows_ has been proposed[^1]. It combines ideas from shadow tomography[^2] and randomized measurement protocols [^3] capable of learning a classical shadow of an unknown quantum state $\rho$. It relies on deliberately discarding the full classical characterization of the quantum state, and instead focuses on accurately predicting a restricted set of properties that provide efficient resources for the study of the system.

A random measurement consists of applying random unitary rotations before a fixed measurement on each copy of a state. Appropriately averaging over these measurements produces an efficient estimator for the expectation value of an observable. This protocol therefore creates a robust classical representation of the quantum state or classical shadow. The captured measurement information is then reuseable for multiple purposes, _i.e._ any observable expected value and available for noise mitigation postprocessing.

A classical shadow is therefore an unbiased estimator of a quantum state $\rho$. Such an estimator is obtained with the following procedure[^1]: first, apply a random unitary gate $U$ to rotate the state: $\rho \rightarrow U \rho U^\dagger$ and then perform a basis measurement to obtain a $n$-bit measurement $|\hat{b}\rangle \in \{0, 1\}^n$. Both unitary gates $U$ and the measurement outcomes $|\hat{b}\rangle$ are stored on a classical computer for postprocessing $U^\dagger |\hat{b}\rangle\langle \hat{b}|U$, a classical snapshot of the state $\rho$. The whole procedure can be seen as a quantum channel $\mathcal{M}$ that maps the initial unknown quantum state $\rho$ to the average result of the measurement protocol:

$$
\mathbb{E}[U^\dagger |\hat{b}\rangle\langle \hat{b}|U] = \mathcal{M}(\rho) \Rightarrow \rho = \mathbb{E}[\mathcal{M}^{-1}(U^\dagger |\hat{b}\rangle\langle \hat{b}|U)]
$$

It is worth noting that the single classical snapshot $\hat{\rho}=\mathcal{M}^{-1}(U^\dagger |\hat{b}\rangle\langle \hat{b}|U)$ equals $\rho$ in expectation: $\mathbb{E}[\hat{\rho}]=\rho$ despite $\mathcal{M}^{-1}$ not being a completely positive map. Repeating this procedure $N$ times results in an array of $N$ independent, classical snapshots of $\rho$ called the classical shadow:

$$
S(\rho, N) = \{ \hat{\rho}_1=\mathcal{M}^{-1}(U_1^\dagger |\hat{b}_1\rangle\langle \hat{b}_1|U_1),\cdots,\hat{\rho}_N=\mathcal{M}^{-1}(U_N^\dagger |\hat{b}_N\rangle\langle \hat{b}_N|U_N)\}
$$

## Running classical shadows

Along the same lines as the example before, estimating the expectation value using classical shadows in Qadence only requires to pass the right set of parameters to the `Measurements` object:

```python exec="on" source="material-block" session="measurements" result="json"
# Classical shadows are defined up to some accuracy and confidence.
from qadence_measurements.utils.data_acquisition import number_of_samples

shadow_options = {"accuracy": 0.1, "confidence": 0.1}
N, K = number_of_samples(observable, shadow_options["accuracy"], shadow_options["confidence"])
shadow_measurement = Measurements(protocol=MeasurementProtocol.SHADOW, options=shadow_options)

# Run the shadow experiment.
estimated_values_shadow = shadow_measurement(model=model)

print(f"Estimated expectation value shadow = {estimated_values_shadow}") # markdown-exec: hide
```

Note that the option `n_shots` is by default 1, which means for one unitary, we sample only once. If we specify a higher
number of shots, more samples are realized per unitary accordingly, and a different formula is used involving the Hamming distance denoted $D$ (see Eq. 2.42 of Ref[^3]):
$$\hat{\rho}^{(r)} = 2^N \bigotimes_{i=1}^N \sum_{b_i} (-2)^{-D[b_i, b_i^{(r)}]} (U^\dagger |\hat{b_i}\rangle\langle \hat{b_i}|U)$$


## Getting shadows

If we are interested in accessing the measurement data from shadows, we can access the measurement data via the `manager` attribute as follows:

```python exec="on" source="material-block" session="measurements" result="json"

measurements_shadows = shadow_measurement.data

print("Sampled unitary indices shape: ", measurements_shadows.unitaries.shape) # markdown-exec: hide
print("Shape of batched measurements: ", measurements_shadows.samples.shape) # markdown-exec: hide
```

In the case of shadows, the measurement data is composed of two elements:
- `unitaries` refers to the indices corresponding to the randomly sampled Pauli unitaries $U$. It is returned as a tensor of shape (shadow_size, n_qubits). Its elements are integer values 0, 1, 2 corresponding respectively to X, Y, Z.
- the second one, `samples`, refers to the bistrings (or probability vectors if `n_shots` is higher than 1) obtained by measurements of the circuit rotated depending on the sampled Pauli basis.
It as returned as a tensor of batched measurements with shape (batch_size, shadow_size, n_qubits) or a tensor of shape (batch_size, shadow_size, $2^n_qubits$) depending on the value of `n_shots`.

Such a measurement data can be used directly for computing different quantities of interest other than the expectation values. For instance, we can do state reconstruction and use it to calculate another expectation value as follows:

```python exec="on" source="material-block" session="measurements" result="json"

# reconstruct state from snapshots
state = shadow_measurement.reconstruct_state()

# calculate expectations
from qadence_measurements.utils.utils_trace import expectation_trace
exp_reconstructed_state = expectation_trace(state, observable)
print(exp_reconstructed_state) # markdown-exec: hide
```

## References

[^1]: [Hsin-Yuan Huang, Richard Kueng and John Preskill, Predicting Many Properties of a Quantum System from Very Few Measurements (2020)](https://arxiv.org/abs/2002.08953)

[^2]: S. Aaronson. Shadow tomography of quantum states. In _Proceedings of the 50th Annual A ACM SIGACT Symposium on Theory of Computing_, STOC 2018, pages 325–338, New York, NY, USA, 2018. ACM

[^3]: Aniket Rath. Probing entanglement on quantum platforms using randomized measurements. Physics \[physics\]. Université Grenoble Alpes \[2020-..\], 2023. English. ffNNT : 2023GRALY072ff. fftel-04523142
