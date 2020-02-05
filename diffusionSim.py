import numpy as np


def diffusionSim(m, n, diffusionRate, t, hotSites, coldSites):
    bar = initBar(m, n, hotSites, coldSites)
    grids = []

    for i in t:
        barExtended = reflectingLat(bar)
        bar = applyDiffusionExtended(diffusionRate, barExtended)
        bar = applyHotCold(bar, hotSites, coldSites)
        grids.append(bar)

    return grids
