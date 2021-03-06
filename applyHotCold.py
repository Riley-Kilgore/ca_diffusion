import numpy as np


def applyHotCold(bar, hotSites, coldSites):
    newBar = bar
    for i in np.size(hotSites):
        xCoord = hotSites[1][1]
        yCoord = hotSites[1][2]
        newBar[xCoord][yCoord] = 2

    for i in np.size(coldSites):
        xCoord = coldSites[1][1]
        yCoord = coldSites[1][2]
        newBar[xCoord][yCoord] = 0

    return newBar
