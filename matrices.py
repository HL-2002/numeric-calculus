from random import randint
class Matrix:
    def __init__(self,n:int):
        # generate a list with random values
        self.list = [[ randint(0,10) for _ in range(n) ] for _ in range(n) ]
        
    def transposed(self):
        # create a new Matrix
        new_matrix = Matrix(len(self.list))
        # iterate a list
        for i in range(len(self.list)):
            for j in range(len(self.list)):
                new_matrix.list[i][j] = self.list[j][i]
        return new_matrix
    
    def __add__(self,other):
        # create a new Matrix
        new_matrix =  Matrix(len(self.list))
        # iterate a list
        for i in range(len(self.list)):
            for j in range(len(self.list)):
                new_matrix.list[i][j] = self.list[i][j] + other.list[i][j]
        return new_matrix
        
        
    def __str__(self):
        # create a string
        str_matrix = ""
        # iterate a list
        for i in  range(len(self.list)):
            for j in  range(len(self.list)):
                str_matrix += "{0:2n} ".format(self.list[i][j])
            str_matrix += "\n"
        return str_matrix
    
    
def main():
    
    try:
        # get a number from stdin
        size_matrix = int(input("Enter size matrix: "))
    except ValueError:
        print("need a number")
        exit()
    # create a matrix
    m1 = Matrix(size_matrix)
    m2 = Matrix(size_matrix)
    # print a matrix
    print("the first matrix is:")
    print(m1)
    print("the second matrix is:")
    print(m2)
    # make a sum
    m3  = m1 + m2
    # print the sum
    print("the result of sum is:")
    print(m3)
    
    print("transposed of result")
    print(m3.transposed())
    
    
    

if __name__ == "__main__":
    main()
