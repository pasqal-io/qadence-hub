# Test Guide

## Lint & Type Check

    pre-commit run --all-files

## Build Documentation

    hatch run docs:build

This will build the root documentation site into the `site/` directory.

## Run Tests

Each module has its own test configuration. For example:

    cd qadence-mitigation
    hatch run test
