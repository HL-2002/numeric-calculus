import numpy as np



def  main():
    #  AX=B
    #  ecuation left side  
    A =  np.array([[-2,5,9],[7,1,1],[-3,7,-1]])
    # ecuation right side
    B =  np.array([1,6,-26])
        
    # result of ecuation x,y,z
    X = np.linalg.solve(A,B)
    print(X)
    
    
    
if __name__ == "__main__":
    main()