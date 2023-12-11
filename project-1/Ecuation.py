import pytest
import sys



def resolve(matrix:list):
    
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if i != j:
                continue
                
            if matrix[i][j] == 0:
                print("no se puede dividir por cero,el sistema no tiene resolucion")
                sys.exit(-1)
            
            if(matrix[i][j] != 1):

                n_elimate = matrix[i][j];
                matrix[i] = [matrix[i][k]/n_elimate for k in range(len(matrix[i])) ]
            for k in range(i+1,len(matrix)):
                n_elimate =  -matrix[k][j]
                invs_matrix = [matrix[i][n] * n_elimate for n in range(len(matrix[i]))]
                matrix[k] = [matrix[k][l] + invs_matrix[l] for l in range(len(matrix[i]))]
                
    for i in range(len(matrix)-1,-1,-1):
        for j in range(len(matrix[i])):
            if i != j:
                continue
            
            for k in range(i-1,-1,-1):
                n_elimate =  -matrix[k][j]
                invs_matrix = [matrix[i][n] * n_elimate for n in range(len(matrix[i]))]
                matrix[k] = [matrix[k][l] + invs_matrix[l] for l in range(len(matrix[i]))]            
    
      
    return [matrix[k][-1] for k in range(len(matrix))]
    
    
    
    
    
# test para verificar que la funcion resuelve correctamente
def test_resolve():
    matrix = [[1,1,-1,0],[2,1,-1,1],[0,-1,1,1]]
    with pytest.raises(SystemExit):
        result = resolve(matrix)
    matrix = [[2,3,1,0],[1,1,2,1],[1,-1,-1,-1]]
    result = resolve(matrix)
    assert pytest.approx(result,rel=0)  == [-1/3, 0, 2/3]
    matrix = [[1,2,2,1],[3,1,2,5],[4,3,3,8]]
    result = resolve(matrix)
    assert pytest.approx(result,rel=0) ==  [13/5, 6/5, -2]
    




def main():
    
    # TODO ADD INPUT USER
    
    matrix = [[1,2,2,1],[3,1,2,5],[4,3,3,8]]
    result = resolve(matrix)
    print(result)
    # TODO ADD verification with numpy
    
    
    
if __name__ == "__main__":
    main()