import numpy as N
from Diffusion import diffusion

def applyDiffusionExtended(ext_lat, diffusion_rate):
    columns = ext_lat.size()[1]
    rows = ext_lat.size()[0]
    new_lat = N.zeros((rows-2,columns-2))
    for i in range(1,rows-1):
        for j in range(1,columns-1):
            new_lat[i,j] = diffusion(diffusion_rate, ext_lat[i,j], ext_lat[i-1,j], ext_lat[i-1,j+1], ext_lat[i,j+1],\
                ext_lat[i+1,j+1], ext_lat[i+1,j], ext_lat[i+1,j-1], ext_lat[i,j-1], ext_lat[i-1,j-1])
    return new_lat