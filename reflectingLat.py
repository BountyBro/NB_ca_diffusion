import numpy as np

def reflectingLat(lat):
    """
    Function to accept a grid and to return a grid extended one cell in each direction with reflecting boundary conditions
    """
    latNS = np.vstack((lat[0, :], lat, lat[-1, :]))
    latR = np.hstack((latNS[:, 0:1], latNS, latNS[:, -1:]))
    return latR