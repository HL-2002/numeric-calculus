from tabulate import tabulate
import sys


def resolve(matrix: list) -> dict:
    """Reduces matrix to row echelon form with Gaussian reduction 
    and solves the system of equations with backward substitution

    Args:
        matrix (list): Augmented matrix of the system of equations

    Returns:
        list: Solution vector
    """
    # Continue for consistent LSE only
    if len(matrix[0])-1 < len(matrix):
        print("Error: SEL inconsistente")
        sys.exit(1)

    # Gaussian Elimination TODO solve negative zeroes in reduced matrix
    # Iterate over the matrix
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if i != j:
                continue

            # Normalize the row by dividing by the diagonal element
            if matrix[i][j] != 0:
                if matrix[i][j] != 1:
                    n_elimate = matrix[i][j]
                    matrix[i] = [matrix[i][k] / n_elimate for k in range(len(matrix[i]))]

                # Perform row operations to eliminate the elements below the diagonal
                for k in range(i + 1, len(matrix)):
                    n_elimate = -matrix[k][j]
                    invs_matrix = [matrix[i][n] * n_elimate for n in range(len(matrix[i]))]
                    matrix[k] = [
                        matrix[k][l] + invs_matrix[l] for l in range(len(matrix[i]))
                    ]

    # Print reduced matrix (Optional)
    print_matrix("Reduced matrix", matrix)

    # Backward Substitution
    solution = [0 for _ in range(len(matrix[0])-1)]

    # Checking for free variables
    if (matrix[-1][-1] == 0 and matrix[-1][-2] == 0):
        solution[-1] = "free"

    # Validate pivots of diagonal, set value as free if not a pivot
    k = 0   # To check the next pivot instead of the usual
    for i in range(len(matrix)):
        free = False # To keep checking for 0
        for j in range(len(matrix[i])-1):
            if (i+k == j or free) and matrix[i][j] == 0:
                solution[i+k] = "free"
                free = True
                k += 1
            else:
                free = False

    # Backward substitution of each pivot
    # Unique solution
    if not("free" in solution):
        for i in range(len(matrix)-1, -1, -1):
            solution[i] = matrix[i][-1]
            for j in range(i+1, len(matrix)):
                solution[i] -= matrix[i][j] * solution[j]
    # Free variables
    else:
        # Loop backwards
        for i in range(len(matrix)-1, -1, -1):
            # Iterate over row, excluding b coefficient
            for j in range(len(matrix[i])-1):
                # Operate if pivot was found
                if matrix[i][j] == 1:
                    # Add coefficient to solution if !=0, make it a str otherwise
                    if matrix[i][-1] != 0:
                        solution[j] = f"{matrix[i][-1]}"
                    else:
                        solution[j] = ""
                    # Evaluate the solution set
                    for k in range(j+1, len(matrix[i])-1):
                        if abs(matrix[i][k]) != 1:
                            solution[j] += f" {-matrix[i][k]:+}*x{k+1}"
                        elif matrix[i][k] == -1:
                            solution[j] += f" +x{k+1}"
                        else:
                            solution[j] += f" -x{k+1}"
                    # Clean output
                    solution[j] = solution[j].strip()
                    break

    # Return the solution vector
    return solution


def print_matrix(name:str, matrix: list) -> None:
    # Headers for the table
    s = [[f"x{i+1}" if i<len(matrix[0])-1 else "b" for i in range(len(matrix[0]))]] 
    # Add the matrix to the table
    s.extend(matrix) 
    # Print tabulated matrix
    print(name, tabulate(s, tablefmt="rounded_outline", headers="firstrow"), sep="\n")


def print_matrix(name:str, matrix: list) -> None:
    # Headers for the table
    s = [[f"x{i+1}" if i<len(matrix[0])-1 else "b" for i in range(len(matrix[0]))]] 
    # Add the matrix to the table
    s.extend(matrix) 
    # Print tabulated matrix
    print(name, tabulate(s, tablefmt="rounded_outline", headers="firstrow"), sep="\n")


def main():
    """
    # Get user's matrix
    matrix = []
    try:
        n = int(input("Cantidad de filas: "))
    except ValueError:
        print("Error: La cantidad de filas debe ser un número entero")
        sys.exit(1)

    for i in range(n):
        # Insert row by row
        row = input(f"Fila {i+1} (x1, x2,..., xn, b): ").split(",")
        # Row validation
        for x in row:
            try:
                x = float(x)
            except ValueError:
                print("Error: Los elementos de la matriz deben ser números")
                sys.exit(1)
        if len(matrix) > 0 and len(matrix[0]) != len(row):
            print("Error: Las filas de la matriz deben tener la misma cantidad de elementos")
            sys.exit(1)
        else: 
            matrix.append(row)

    # Print user's matrix
    print_matrix("Matriz ingresada", matrix)
    """

    """ This is for testing purposes, need to adapt user's instead of hardcoded matrix """
    # Resolve and print solution vector
    matrix = [[1, 1, -1, 0], 
              [2, 1, -1, 1], 
              [0, -1, 1, 1]]
    #matrix= [[2, 3, 1, 0], 
    #          [1, 1, 2, 1], 
    #          [1, -1, -1, -1]]
    solution = resolve(matrix)
    print(*[f"x{i+1} = {solution[i]}" for i in range(len(solution))], sep="\n")


if __name__ == "__main__":
    main()
