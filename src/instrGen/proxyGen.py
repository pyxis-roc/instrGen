import argparse
import subprocess
import os
import sys

def get_proxy(input_file, target_function, output_file='proxy.ll'):
    # use symCount to generate proxy IR for the given LLVM IR file
    with open(output_file, 'w') as f:
        subprocess.run(
            [
                'symCount', 
                input_file, 
                target_function
            ], 
            stdout=sys.stdout, 
            stderr=f
        )

def gnerate(input_file, output_file):
    output_suffix = os.path.splitext(output_file)[1]

    if output_suffix == '.ll':
        result = subprocess.run(
            [
                'clang++', 
                '-emit-llvm', 
                '-S', 
                input_file, 
                '-o', 
                output_file
            ], 
            stdout=sys.stdout, 
            stderr=sys.stderr
        )
    
    elif output_suffix == '':
        result = subprocess.run(
            [
                'clang++', 
                input_file, 
                '-o', 
                output_file
            ], 
            stdout=sys.stdout, 
            stderr=sys.stderr
        )
        
    elif output_suffix == '.o':
        result = subprocess.run(
            [
                'clang++', 
                '-c', 
                input_file, 
                '-o', 
                output_file
            ], 
            stdout=sys.stdout, 
            stderr=sys.stderr
        )

    elif output_suffix == '.so':
        result = subprocess.run(
            [
                'clang++', 
                '-shared', 
                input_file, 
                '-o', 
                output_file
            ], 
            stdout=sys.stdout, 
            stderr=sys.stderr
        )

def cli():
    
    parser = argparse.ArgumentParser(description='Generate proxy for a given LLVM IR file')
    parser.add_argument('input', type=str, help='Input LLVM IR file')
    parser.add_argument('target_function', type=str, help='Target function name')
    parser.add_argument('output',default='proxy.ll', type=str, help='Output .ll or .o or .so file, default to proxy.ll')

    args = parser.parse_args()

    input_file = args.input
    proxy_file = os.path.splitext(input_file)[0] + '_proxy.ll'
    get_proxy(input_file, args.target_function, proxy_file)

    output_file = args.output
    gnerate(proxy_file, output_file)