import numpy as np

AMBIENT = 25
HOT = 50
COLD = 0

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
    m, n = bar.shape
    for i in range(m):
        for j in range(n):
            if (i, j) in hotSites:
                bar[i, j] = HOT
            elif (i, j) in coldSites:
                bar[i, j] = COLD
    return bar