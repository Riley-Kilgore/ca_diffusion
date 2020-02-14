__author__ = 'v-caearl'

import numpy as np


def diffusion(diffusionRate, site, N, NE, E, SE, S, SW, W, NW):
    # mean and standard deviation
    mu = 0
    sigma = 0.5

    # creates 8 samples normally distributed, one for each site to account for imperfections in RL diffusion
    r = np.random.normal(mu, sigma, 8)

    # revises the coefficient for site to exactly account for the differences in the f (diffusion rate) value
    site = site * np.mean(r)

    return (1-8*diffusionRate)*site + (1 + r[0]) * diffusionRate * N + (1 + r[1]) * diffusionRate * NE + \
           (1 + r[2]) * diffusionRate * E + (1 + r[3]) * diffusionRate * SE + (1 + r[4]) * diffusionRate * S + \
           (1 + r[5]) * diffusionRate * SW + (1 + r[6]) * diffusionRate * W + (1 + r[7]) * diffusionRate * NW
