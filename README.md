# instrumentation generator

## Description
It provides two simple wrappers to facilitate LLVM IR instrumentation.

`instrGen` calls LLVM PGO instrumentation on the input LLVM IR.

`proxyGen` calls symbolic proxy on the input LLVM IR.

Output format can be .ll .so .o or executable

## Installation

```bash
python3 -m pip install -e .
```

## Usage
### instrGen 

```bash
usage: instrGen [-h] input [input ...] output
instrGen: error: the following arguments are required: input, output

instrGen mm.ll mm-instr.so
```

### proxyGen

#### Requirements
Before installation, ensure you have cloned and installed the Trip Counter repository:
git@github.com:pyxis-roc/trip_counter.git

```bash
usage: proxyGen [-h] input target_function output
proxyGen: error: the following arguments are required: input, output

proxyGen mm.ll mm mm-proxy.so
```
