import argparse
import subprocess
import os
import sys


def generate(input_file, output_file):
    output_suffix = os.path.splitext(output_file)[1]

    if output_suffix == ".ll":
        result = subprocess.run(
            [
                "clang",
                "-fprofile-generate",
                "-emit-llvm",
                "-S",
                *input_file,
                "-o",
                output_file,
            ],
            stdout=sys.stdout,
            stderr=sys.stderr,
        )

    elif output_suffix == "":
        result = subprocess.run(
            ["clang", "-fprofile-generate", *input_file, "-o", output_file],
            stdout=sys.stdout,
            stderr=sys.stderr,
        )

    elif output_suffix == ".o":
        result = subprocess.run(
            ["clang", "-fprofile-generate", "-c", *input_file, "-o", output_file],
            stdout=sys.stdout,
            stderr=sys.stderr,
        )

    elif output_suffix == ".so":
        result = subprocess.run(
            [
                "clang",
                "-fprofile-generate",
                "-fPIC",
                "-shared",
                *input_file,
                "-o",
                output_file,
            ],
            stdout=sys.stdout,
            stderr=sys.stderr,
        )


def main():
    parser = argparse.ArgumentParser(
        description="Generate LLVM PGO instrumentation code for a given LLVM IR file"
    )
    parser.add_argument("input", nargs="+", help="Input LLVM IR file(s)")
    parser.add_argument(
        "output",
        default="instr.ll",
        type=str,
        help="Output .ll or .o or .so file, default to instr.ll",
    )

    args = parser.parse_args()

    input_file = args.input
    output_file = args.output

    generate(input_file, output_file)
