Sparse Matrix Implementation
Overview
This project implements a sparse matrix data structure and operations in Python, as specified for Programming Assignment 2. The implementation uses a dictionary-based coordinate list (COO) format to efficiently store and manipulate large sparse matrices. The code supports reading matrices from files, performing addition, subtraction, and multiplication, and saving results to an output file. It handles input file variations (e.g., whitespace) and includes error checking for invalid formats.
Features

SparseMatrix Class: Stores non-zero elements in a dictionary with (row, col) keys, optimizing memory usage.
File Input/Output: Reads matrices from files in the format rows=<num>, cols=<num>, followed by (row, col, value) entries. Outputs results in the same format.
Operations: Supports matrix addition, subtraction, and multiplication with dimension validation.
Error Handling: Throws ValueError for invalid file formats, dimensions, or indices.
Command-Line Interface: Allows users to select an operation and specify input/output file paths.

Directory Structure
/dsa/sparse_matrix/
├── code/
│   └── src/
│       └── sparse_matrix.py
├── sample_inputs/
│   └── (input files, e.g., matrix1.txt, matrix2.txt)
└── README.md

Requirements

Python 3.6 or higher
No external libraries are required (uses only built-in Python modules: open for file I/O).

Installation

Clone or download this repository to your local machine.
Ensure the directory structure matches the one above.
Place input matrix files in the sample_inputs directory. These files should follow the format:rows=<number>
cols=<number>
(row, col, value)
...

Example:rows=8433
cols=3180
(0, 381, -694)
(0, 128, -838)



Usage

Navigate to the code/src directory:cd /dsa/sparse_matrix/code/src


Run the script using Python:python sparse_matrix.py


Follow the prompts:
Select an operation (1 for addition, 2 for subtraction, 3 for multiplication).
Enter the file paths for the two input matrices (e.g., ../../sample_inputs/matrix1.txt).
Enter the output file path (e.g., ../../output.txt).


The program will perform the selected operation and save the result to the specified output file in the same format as the input.

Example interaction:
Sparse Matrix Operations
1. Addition
2. Subtraction
3. Multiplication
Select operation (1-3): 1
Enter first matrix file path: ../../sample_inputs/matrix1.txt
Enter second matrix file path: ../../sample_inputs/matrix2.txt
Enter output file path: ../../output.txt
Result saved to ../../output.txt

Error Handling
The program handles the following errors:

Invalid file format (e.g., missing rows= or cols=, non-integer values, incorrect parentheses).
File not found.
Invalid matrix dimensions for operations (e.g., mismatched dimensions for addition/subtraction, or incompatible dimensions for multiplication).
Out-of-bounds row or column indices.

Errors are reported with descriptive messages, e.g., Error: Input file has wrong format.
Implementation Details

Data Structure: Uses a Python dictionary to store non-zero elements, with (row, col) tuples as keys and values as integers. This ensures memory efficiency for sparse matrices.
Operations:
Addition/Subtraction: Combines elements from both matrices, storing only non-zero results.
Multiplication: Computes the product of two matrices, iterating only over non-zero elements.


File Parsing: Skips empty lines, handles whitespace, and validates input format.
Sorting: Output is sorted by row, then column, for consistent file output.

Notes

The code avoids external libraries, using only built-in Python functionality.
The implementation is tested with sample input files from the provided Google Drive link: https://drive.google.com/drive/folders/17JkqxKGo0x9LD5hjdbpPoIGOCEmq9SGJ.
Ensure input files are correctly formatted to avoid errors.
The code is designed to handle large matrices efficiently by storing only non-zero elements.

Author
This implementation was created as part of Programming Assignment 2 for a Data Structures and Algorithms course.
License
This project is for educational purposes and follows the guidelines of the assignment.

