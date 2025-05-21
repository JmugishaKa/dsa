Sparse Matrix Implementation

Table of contents:
1.Overview.
2.Features.
3.Directory structure.
4.Installation.
5.Usage.
6.Notes.
7.Author.

--------------------------------------------------
Overview

This project implements a sparse matrix data structure and operations in Python. The code allows and supports reading matrices from files, performing addition(+), subtraction(-), and multiplication(*), and saves the feedback to output file.
-------------------------------------------------------
Features

Class of SparseMatrix : To Store non-zero elements in a dictionary together with (row, col) keys.
Error Handling: Throws ValueError for invalid file formats, dimensions, or indices.
Operations: Supports matrix addition, subtraction, and multiplication with dimension validation.
File I/O: To allow reading of matrices in the  rows=<num>, cols=<num> format with (row, col, value) following.
Command-Line Interface: Allow users to choose an operation and input/output file paths.

------------------------------------------------------------
Directory Structure

/dsa/sparse_matrix/
                   ├──code/ src/ sparse_matrix.py
                   ├── sample_inputs/input files
                   |── README.md
-----------------------------------------------------------

Installation

Clone or download the repository to your local machine.
Ensure the directory structure looking perfectly like the one above in the structure.
Put input matrix files in  sample_inputs dir. Those files need to follow the order:
rows=<number>
cols=<number>
(row, col, value)
...

Example:rows=8433
cols=3180
(0, 381, -694)
(0, 128, -838)

-------------------------------------------------------
Usage

Navigate to the code/src directory:cd /dsa/sparse_matrix/code/src

Run the script using Python:python sparse_matrix.py

Following the instructions from the prompts:
Select an operation (1 (addition), 2 (subtraction), 3 (multiplication)).
Enter the file paths (e.g., ../../sample_inputs/easy_sample_01_2.txt).
Enter the output file path (e.g., ../../output.txt).


Example:
Sparse Matrix Operations
1. Addition
2. Subtraction
3. Multiplication
Select operation (1-3): 1
Enter first matrix file path: ../../sample_inputs/easy_sample_01_2.txt
Enter second matrix file path: ../../sample_inputs/easy_sample_01_3.txt
Enter output file path: ../../output.txt
Result saved to ../../output.txt
---------------------------------------------------------------
Error Handling
The program handles the following errors:

Invalid file format (e.g.incorrect parentheses, non-integer values,... ).

File not being found.

Out-of-bounds row or column indices.

Errors are reportedusing short messages, like, Error: Input file has wrong format.
----------------------------------------------------------------------
Notes:
.The code uses built-in Python functionality only.

.The implementation of the code is tried on sample input files from the google drive link: https://drive.google.com/drive/folders/17JkqxKGo0x9LD5hjdbpPoIGOCEmq9SGJ.

.Ensuring input files are well-formatted to avoid errors.

.The code will handle large matrices, by storing only non-zero elements effectively.
--------------------------------------
Author:
Joshua Mugisha, BSc Software Engineering ALU.



