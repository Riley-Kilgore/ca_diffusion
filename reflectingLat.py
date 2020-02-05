def reflectingLat(lat):

    # reflect top/bottom
    for i in range(1, len(lat[0]) - 1):
        lat[0][i] = lat[1][i]
        lat[len(lat) - 1][i] = lat[len(lat) - 2][i]
    
    # reflect left/right
    for i in range(1, len(lat) - 1):
        lat[i][0] = lat[i][1]
        lat[i][len(lat[0]) - 1] = lat[i][len(lat[0]) - 2]

    # set corners
    lat[0][0] = lat[1][1]
    lat[0][1] = lat[1][1]
    lat[0][len(lat[0]) - 1] = lat[1][len(lat[0]) - 2]
    lat[0][len(lat[0]) - 2] = lat[1][len(lat[0]) - 2]

    lat[len(lat) - 1][0] = lat[len(lat) - 2][1]
    lat[len(lat) - 1][1] = lat[len(lat) - 2][1]
    lat[len(lat) - 1][len(lat[0]) - 1] = lat[len(lat) - 2][len(lat[0]) - 2]
    lat[len(lat) - 1][len(lat[0]) - 2] = lat[len(lat) - 2][len(lat[0]) - 2]

    return lat
