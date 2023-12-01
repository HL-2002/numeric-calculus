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
    ay = ax-2
    by = bx+2
    params = 21
    
    xi = np.linspace(ax,bx,params)
    yi = np.linspace(ay,by,params)
    
    # generate grid
    Xi,Yi = np.meshgrid(xi,yi)
        
    # evalute cordinate
    Z0 = z0(Xi,Yi)
    Z1 = z1(Xi,Yi)
    Z2 = z2(Xi,Yi)
    
    
    
    
    # create a figure
    figure = plt.figure()
    graph = figure.add_subplot(111, projection='3d')
    
    # add planes
    graph.plot_wireframe(Xi,Yi,Z0,
                       color ='blue',
                       label='Ecuación 1')
    graph.plot_wireframe(Xi,Yi,Z1,
                         color='green'
                         ,label='Ecuación 2')    
    graph.plot_wireframe(Xi,Yi,Z2,
                        color='orange',
                        label='Ecuación 3')
    

    plt.show()
        
        
        
    # result of ecuation x,y,z
    X = np.linalg.solve(A,B)
    print(X)
    
    
    
if __name__ == "__main__":
    main()