import numpy as np
import fins

#  Input Data #
Lx = 26
Ly = 30
dx = 0.1
dy = 0.1
dt = 0.01
tmax = 10

# Fin Data #
finWidth = 1
finGap =  1
finHeight = 10
baseHeight = 1
depth = 10

Nx = int(Lx/dx) + 1
Ny = int(Ly/dy) + 1
numTimesteps = int(tmax/dt)

T = np.zeros((Ny, Nx, numTimesteps))

#Mask map used to identify solid (0) or liquid (1)
maskMap = np.ones((Ny, Nx))
maskMap = fins.GenerateFins(maskMap, Lx, Ly, Nx, Ny, dx, dy, finWidth, finGap, finHeight, baseHeight)
fins.VisualizeFins(np.flip(np.fliplr(maskMap)), Lx, Ly, 0, finHeight)

###############################################################





