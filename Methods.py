import numpy as np

##Helpers
def CalculateCentralDifference(F, dx, dy):
    dFdx = (F[2:, 1:-1] - F[:-2, 1:-1])/(2*dx)
    dFdy = (F[1:-1, 2:] - F[1:-1, :-2])/(2*dy)
    return dFdx, dFdy

def CalculateCentralDifference2nd(F, dx, dy):
    ddFdx = (F[2:, 1:-1] - 2 * F[1:-1, 1:-1] + F[:-2, 1:-1])/(2*dx)
    ddFdy = (F[1:-1, 2:] - 2 * F[1:-1, 1:-1] + F[1:-1, :-2])/(2*dy)
    return ddFdx, ddFdy

def ImplicitSolveNavierStokes(u, v, p, Nx, Ny, dx, dy, dt, L):
    u = u.reshape(-1, 1)
    v = v.reshape(-1, 1)

    #Get pressure and set up RHS
    dpdx, dpdy = CalculateCentralDifference(p, dx, dy)

    bx = -dpdx * np.ones((Nx * Ny, 1)) + u
    by = -dpdy * np.ones((Nx * Ny, 1)) + v

    #Gonna have to do some picard iteration
    tol = 1e-2

    for i in range(30):

        #Have to build new matrix each iteration
        A = BuildMatrix(u, v, Nx, Ny, dx, dy, dy, L)

        #Should probably replace with a better solver here
        um = np.linalg.inv(A) @ bx
        vm = np.linalg.inv(A) @ by

        #du = np.mean(np.abs((u - um)))
        #dv = np.mean(np.abs((v - vm)))

        #delta = max(du, dv)

        u = um
        v = vm

    u = u.reshape(Ny, Nx)
    v = v.reshape(Ny, Nx)

    return u, v

def BuildMatrix(u, v, Nx, Ny, dx, dy, dt, L):
    size = Nx * Ny - 2
    
    betax = (dt * L)/ dx**2
    betay = (dt * L)/ dy**2
    
    Cx = dt/(2 * dx)
    Cy = dt/(2 * dy)

    #i,j
    A = (1 + 2*betax + 2*betay) * np.identity(size) 
    #i+1, j
    A += (Cx * u[1:-1] - betax) * np.eye(size, k = 1) 
    #i-1, j
    A += (-Cx * u[1:-1] - betax) * np.eye(size, k = -1) 
    #i, j+1
    A += (Cy * v[1:-1] - betay) * np.eye(size, k = Nx) 
    #i, j-1
    A += (-Cx * v[1:-1] - betay) * np.eye(size, k = -Nx)

    
