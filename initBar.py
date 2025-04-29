import numpy as np
# Global constants

AMBIENT = (128, 128, 128)
HOT = (0, 0, 0)
COLD = (255, 255, 255)

def initBar(m, n, hotSites, coldSites):
    """
    initializes a bar with ambient temperature
    """
    ambientBar = np.full((m, n), AMBIENT)
    return applyHotCold(ambientBar, hotSites, coldSites)

def applyHotCold(bar, hotSites, coldSites):
    """
    Assigns hot and cold temperatures to the bar
    """
    new_bar = bar
    m, n = new_bar.shape
    for i in range(m):
        for j in range(n):
            if (i, j) in hotSites:
                new_bar[i, j] = HOT
            elif (i, j) in coldSites:
                new_bar[i, j] = COLD
    return new_bar