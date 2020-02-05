import numpy as np
from applyHotCold import applyHotCold

# creates extra space (1-cell border) for boundery
def initBar(width, height, hotsites, coldsites):
    amb_temp = 1
    bar = np.ones((height + 2, width + 2), dtype=int)
    bar = bar * amb_temp

    return applyHotCold(amb_temp, hotsites, coldsites)

