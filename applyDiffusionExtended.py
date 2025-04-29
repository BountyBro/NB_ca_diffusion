import numpy as np
import matplotlib.pyplot as plt

def applyDefusionExtended(diff_r, latExt):
  toReturn = np.full(shape= latExt.shape, fill_value= (255, 0, 0))
  rows, cols = tuple(np.subtract(latExt.shape, (2, 2)))  # Uses numpy tuple unpacking and subtraction to define true rows and cols.
  for row in range(1, rows + 2):
    for col in range(1, cols + 2):
        toReturn[row, col] = tuple( 5.1 * diffusion(diff_r, latExt[row, col], latExt[row - 1, col], latExt[row - 1, col + 1], latExt[row, col + 1], latExt[row + 1, col + 1], latExt[row + 1, col], latExt[row + 1, col - 1], latExt[row - 1, col], latExt[row - 1, col - 1]) for i in range(3))
  return toReturn      
