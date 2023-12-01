import numpy as np
import matplotlib.pyplot as plt


def  main():
    #  AX=B
    #  ecuation left side  
    A =  np.array([[-2,5,9],[7,1,1],[-3,7,-1]])
    # ecuation right side
    B =  np.array([1,6,-26])
        
    # define plane ecuation 
    z0 = lambda x,y: ( - A[0,0]*x - A[0,1]*y + B[0]) / A[0,2] 
    z1 = lambda x,y: ( - A[1,0]*x - A[1,1]*y + B[1]) / A[1,2] 
    z2 = lambda x,y: ( - A[2,0]*x - A[2,1]*y + B[2]) / A[2,2] 
    
    # generate range for x and y
    ax = -5
    bx = 5
    ay = -7
    by = 7
    params = 21
    
    xi = np.linspace(ax,bx,params)
    yi = np.linspace(ay,by,params)
    
    # generate grid
    X,Y = np.meshgrid(xi,yi)
        
    # evalute cordinate
    Z0 = z0(X,Y)
    Z1 = z1(X,Y)
    Z2 = z2(X,Y)
    
    
        
        
        
    # result of ecuation x,y,z
    X = np.linalg.solve(A,B)
    print(X)
    
    
    
if __name__ == "__main__":
    main()