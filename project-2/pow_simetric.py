import numpy as np


def method_pow_simetric(matrix : np.matrix ,interactions:int)-> tuple:
    """
    Calculates the dominant eigenvector and eigenvalue of a symmetric matrix using the power iteration method.

    Parameters:
    matrix (np.matrix): The symmetric matrix.
    interactions (int): The number of iterations to perform.

    Returns:
    tuple: A tuple containing the dominant eigenvector and eigenvalue.
    """
    
    # check if the matrix is simetric
    if not ( np.equal(matrix,matrix.T).all() or  matrix.shape[0] == matrix.shape[1] ):
        print("The matrix is not simetric")
        exit(0)
 
    # vector 
    initial  = np.random.rand(matrix.shape[0],1)
    # first iteration

    matrix2 = np.dot(matrix,initial) / np.linalg.norm(np.dot(matrix,initial))
    for _ in range(interactions):
        yx_ml = matrix2
        x_k = np.dot(matrix,matrix2)
        matrix2 = x_k / np.linalg.norm(x_k)
    
    

    return matrix2, np.dot(np.dot(matrix,yx_ml).T,yx_ml) / np.dot(yx_ml.T,yx_ml)
    
    
    
    

def test():
    m = np.matrix([[3.556, -1.778,0], [-1.778, 3.556,-1.778], [0,-1.778,3.556]])
    eigvector,eigvalor = method_pow_simetric(m, 5000)
    print(f"The dominant eigenvector is: \n{eigvector}")
    print(f"The dominant eigenvalue is: \n{eigvalor}")


if __name__ == "__main__":
    test()







