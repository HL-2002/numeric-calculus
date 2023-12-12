import pytest
import numpy as np
from equation import resolve

@pytest.fixture
def solvable_matrix():
    return [[2, 3, 1, 0], 
            [1, 1, 2, 1], 
            [1, -1, -1, -1]]

# Test function to verify that the resolve function works correctly
def test_resolve(solvable_matrix):
    # Test unsolvable system
    matrix = [[1, 1, -1, 0], 
              [2, 1, -1, 1], 
              [0, -1, 1, 1],
              [0, 1, -1, 2]]
    with pytest.raises(SystemExit):
        result = resolve(matrix)

    # Test system with infinite solutions
    matrix = [[1,3,1,2,7],
              [0,0,1,4,-1],
              [0,0,0,0,0]]
              
    assert resolve(matrix) == ["7 -3*x2 -x3 -2*x4", "free", "-1 -4*x4" ,"free"]

    # Test solvable systems
    result = resolve(solvable_matrix)
    assert pytest.approx(result) == [-1 / 3, 0, 2 / 3]

    matrix = [[1, 2, 2, 1], 
              [3, 1, 2, 5], 
              [4, 3, 3, 8]]
    result = resolve(matrix)
    assert pytest.approx(result) == [13 / 5, 6 / 5, -2]

# Test resolve with numpy equivalent
def test_numpy_validation(solvable_matrix):
    a = np.array([[2, 3, 1], 
                  [1, 1, 2], 
                  [1, -1, -1]])
    b = [solvable_matrix[i][-1] for i in range(len(solvable_matrix))]

    assert np.linalg.solve(a,b) == pytest.approx(resolve(solvable_matrix))
