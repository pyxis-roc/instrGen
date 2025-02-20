# instrumentation generator

## Description
A simple wrapper to call clang PGO instrumentation Gen pass that accepts one or multiple llvm IR files and generate instrumented version. Output format can be .ll .so .o or executable

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)

## Installation

```bash
python3 -m pip install -e .
```

## Usage
Examples of how to use the project.

```bash
usage: instrGen [-h] input [input ...] output
instrGen: error: the following arguments are required: input, output

instrGen mm.ll mm.so
```