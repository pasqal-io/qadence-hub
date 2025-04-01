# ⚙️ Setup Guide

## 1. Clone the Monorepo

    git clone https://github.com/pasqal-io/qadence-hub.git
    cd qadence-hub

## 2. Navigate to the directory for the project you want to work on:

- **For protocols development**:

    cd test-qadence-protocols

- **For libs development**:

    cd test-qadence-libs


## 3. Enter the Hatch environment

We use [Hatch](https://hatch.pypa.io) to manage development environments and builds.
To set up and enter the environment, run:

    hatch env create
    hatch shell
