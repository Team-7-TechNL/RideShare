from geopy import distance

if __name__ == "__main__":
    import RideshareGUI


def distchecker(Clientcords):
    dist = {}
    # TODO Replace Cords with the drivers locations
    cords = [(47.51044931589316, -52.92471902671029),
             (47.50997182304524, -52.924989780304585),
             (47.5117538621506, -52.92535888029291),
             (47.51239826716989, -52.92605581737727),
             (47.5119085248456, -52.92771487525117),
             (47.51798725653911, -52.933987077831056),
             (47.52029535370516, -52.93654879275768)]
    count = 0
    for i in cords:
        count += 1
        x = distance.distance(i, Clientcords)
        dist[i] = x
    min_dist = min(dist.values())
    key_list = list(dist.keys())
    val_list = list(dist.values())
    position = val_list.index(min_dist)
    return key_list[position]
