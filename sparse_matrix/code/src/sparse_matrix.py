# My Sparse Matrix Program for HW01.
# Would Handle big matrices with mostly zeros.
# I will use a dictionary to store only non-zero values to save space.
# Needs to include error checking.

# deifinig a class function
class MatrixSparse:
    def __init__(self, input_file=None, num_rows=None, num_cols=None): 
# Set up the matrix, either from a file or just with dimensions
        self.values = {}  # For (row, col) -> value for non-zeros
        self.rows = 0
        self.cols = 0
        if input_file:
            self.load_matrix(input_file)  # Reading from the file
        else:
            if not num_rows or not num_cols or num_rows <= 0 or num_cols <= 0:
                raise ValueError("Need valid row and column numbers!")
            self.rows = num_rows
            self.cols = num_cols

    def load_matrix(self, file_path):
        # Reads the file with rows=<num>, cols=<num>, and (row,col,value) lines
        try:
            with open(file_path, 'r') as f:
                # First line should be rows=
                first_line = f.readline().strip()
                if not first_line.startswith("rows="):
                    raise ValueError("File doesn't start with 'rows='")
                self.rows = int(first_line[5:])
                if self.rows <= 0:
                    raise ValueError("Rows must be positive")

                # Second line should be cols=
                second_line = f.readline().strip()
                if not second_line.startswith("cols="):
                    raise ValueError("File doesn't have 'cols=' on second line")
                self.cols = int(second_line[5:])
                if self.cols <= 0:
                    raise ValueError("Columns must be positive")

                # Process each data line
                for line in f:
                    line = line.strip()
                    if line == "":  # Ignore blank lines
                        continue
                    # Check for (row, col, value) format
                    if not line.startswith("(") or not line.endswith(")"):
                        raise ValueError("Line must be in (row, col, value) format")
                    
                    # Remove ( and ) and split by commas
                    clean_line = line[1:-1]
                    parts = [p.strip() for p in clean_line.split(",")]
                    if len(parts) != 3:
                        raise ValueError("Each line needs exactly 3 values")

                    # Make sure row, col, value are integers
                    for p in parts:
                        if not p:
                            raise ValueError("Values can't be empty")
                        if p[0] == "-" and len(p) > 1:
                            if not p[1:].isdigit():
                                raise ValueError("Values must be integers")
                        elif not p.isdigit():
                            raise ValueError("Values must be integers")

                    row = int(parts[0])
                    col = int(parts[1])
                    val = int(parts[2])

                    # Validate indices and value
                    if row < 0 or row >= self.rows or col < 0 or col >= self.cols:
                        raise ValueError("Row or column out of bounds")
                    if val == 0:  # Don't store zeros
                        raise ValueError("Zero values not allowed in file")

                    # Save the value
                    self.values[(row, col)] = val

        except FileNotFoundError:
            raise ValueError("Couldn't find the input file")

    def get_value(self, row, col):
        # Get value at position (row, col), return 0 if empty
        if row < 0 or row >= self.rows or col < 0 or col >= self.cols:
            raise ValueError("Row or column index is invalid")
        return self.values.get((row, col), 0)

    def set_value(self, row, col, value):
        # Set value at (row, col), remove if it's 0
        if row < 0 or row >= self.rows or col < 0 or col >= self.cols:
            raise ValueError("Row or column index is invalid")
        if value == 0:
            self.values.pop((row, col), None)  # Remove if exists
        else:
            self.values[(row, col)] = value

    def add_matrices(self, other):
        # Add this matrix to another one
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrices must have same size for addition")
        
        result = MatrixSparse(num_rows=self.rows, num_cols=self.cols)
        # Add my values
        for pos, val in self.values.items():
            result.set_value(pos[0], pos[1], val)
        # Add other matrix's values
        for pos, val in other.values.items():
            current = result.get_value(pos[0], pos[1])
            result.set_value(pos[0], pos[1], current + val)
        return result

    def subtract_matrices(self, other):
        # Subtract other matrix from this one
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrices must have same size for subtraction")
        
        result = MatrixSparse(num_rows=self.rows, num_cols=self.cols)
        # Copy my values
        for pos, val in self.values.items():
            result.set_value(pos[0], pos[1], val)
        # Subtract other values
        for pos, val in other.values.items():
            current = result.get_value(pos[0], pos[1])
            result.set_value(pos[0], pos[1], current - val)
        return result

    # Multiply the matrix by another matrices
    def multiply_matrices(self, other):
       
        if self.cols != other.rows:
            raise ValueError("Number of columns in first matrix must equal rows in second")
        
        result = MatrixSparse(num_rows=self.rows, num_cols=other.cols)
        # Looping into non-zero elements
        for (i, k), val1 in self.values.items():
            for (k2, j), val2 in other.values.items():
                if k == k2:  # Matching first column with second row
                    current = result.get_value(i, j)
                    result.set_value(i, j, current + val1 * val2)
        return result

    def write_to_file(self, file_path):
        # Saving  the matrix  to a file from the provided path
        with open(file_path, 'w') as f:
            f.write(f"rows={self.rows}\n")
            f.write(f"cols={self.cols}\n")
                             # Sorting first by row and then column for a good output
            for row, col in sorted(self.values.keys()):
                f.write(f"({row}, {col}, {self.values[(row, col)]})\n")

# Prompt steps to allow user select an operation and files
def run_program():
    print("Sparse Matrix Program")
    print("1) Add two matrices")
    print("2) Subtract two matrices")
    print("3) Multiply two matrices")
    
    choice = input("Pick an option (1, 2, or 3): ").strip()
    if choice not in ["1", "2", "3"]:
        print("That's not a valid option!")
        return
    
    file_a = input("Enter first matrix file: ").strip()
    file_b = input("Enter second matrix file: ").strip()
    out_file = input("Enter output file name: ").strip()

    try:
        # Load the  matrices from the file
        mat1 = MatrixSparse(input_file=file_a)
        mat2 = MatrixSparse(input_file=file_b)

        # To be done on the operation selected by the user
        if choice == "1":
            result = mat1.add_matrices(mat2)
        elif choice == "2":
            result = mat1.subtract_matrices(mat2)
        else:
            result = mat1.multiply_matrices(mat2)

        
        # Saving the response to be given
        result.write_to_file(out_file)
        print(f"Output saved to {out_file}")

    
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Oops, something broke: {e}")


if __name__ == "__main__":
    run_program()
