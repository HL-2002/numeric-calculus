from random import randint
from tabulate import tabulate

# Matrix class
class Matrix():
    
    # Initialize matrix with random numbers
    def __init__(self, n):
        self.n = n
        self.content = [[randint(0,10) for _ in range(n)] for _ in range(n)]

    # Transpose support, modifies matrix's content
    def transpose(self) -> None:
        transpose = Matrix(self.n)
        for i in range(self.n):
            for j in range(self.n):
                transpose.content[i][j] = self.content[j][i]

        self.content = transpose.content


    # Addition support
    def __add__(self, other):
        matrix = Matrix(self.n)
        for i in range(self.n):
            for j in range(self.n):
                matrix.content[i][j] = self.content[i][j] + other.content[i][j]

        return matrix

    # Str for printing
    def __str__(self):
        return tabulate(self.content, tablefmt="simple_grid")


def main():
    while True:
        try:
            n = int(input("N(int): "))
        except ValueError:
            continue
        else:
            break


    m1 = Matrix(n)
    print("m1:\n", m1, sep="")
    m2 = Matrix(n)
    print("m2:\n", m2, sep="")

    m3 = m1+m2

    print("m3:\n", m3, sep="")

    m3.transpose()

    print("m3 transpose:\n", m3, sep="")

if __name__ == "__main__":
    main()