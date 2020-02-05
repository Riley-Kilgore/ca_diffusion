import numpy as np

# creates extra space (1-cell border) for boundery
def initBar(width, height):
    return np.zeros((height + 2, width + 2), dtype=float)

