import matplotlib.pyplot as plt

def GenerateFins(maskMap, Lx, Ly, Nx, Ny, dx, dy, finWidth, finGap, finHeight, baseHeight):
    
    if (finHeight + baseHeight > Lx):
        return "Fin height too large"
    
    if (finWidth + finGap > Nx):
        return "Fins too large"
    
    finNodeWidth = int(finWidth/dx)
    finNodeGap = int(finGap/dx)
    baseNodeHeight = int(baseHeight/dy)
    finNodeHeight = baseHeight + int(finHeight/dy)

    finCount = int(Nx/(finNodeWidth + finNodeGap))
    #Setup base
    maskMap[:baseNodeHeight, :] = 0

    for fin in range(finCount):
        for finNode in range(finNodeWidth):
            maskMap[baseNodeHeight:finNodeHeight, finNode + fin*(finNodeWidth + finNodeGap)] = 0

    return maskMap

def VisualizeFins(maskMap, Lx, Ly, finCount, finHeight):
    plt.figure()
    cp = plt.imshow(maskMap, cmap="gray_r", interpolation=None, extent=[0, Lx, 0, Ly])
    plt.colorbar(cp)
    plt.title("Visualization of Fins")
    plt.xlabel("X (mm)")
    plt.ylabel("Y (mm)")
    plt.show()
