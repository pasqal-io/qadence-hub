# Setup Guide

## 1. Clone Qadence-Hub
```shell
git clone https://github.com/pasqal-io/qadence-hub.git
cd qadence-hub
```

## 2. Navigate to the directory for the project you want to work on:

- **For mitigations development**:
```shell
cd qadence-mitigation
```

- **For commons development**:
```shell
cd qadence-commons
```

## 3. Enter the Hatch environment

We use [Hatch](https://hatch.pypa.io) to manage development environments and builds.
To set up and enter the environment, run:
```shell
hatch env create
hatch shell
```
