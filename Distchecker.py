from geopy import distance
from main import Mapmain
closetsdriver = 0

def distchecker(*clientcords):
    global closetsdriver

    latlong = [(47.51044931589316, -52.92471902671029),
               (47.50997182304524, -52.924989780304585),
               (47.5117538621506, -52.92535888029291),
               (47.51239826716989, -52.92605581737727),
               (47.5119085248456, -52.92771487525117),
               (47.51798725653911, -52.933987077831056),
               (47.52029535370516, -52.93654879275768)]
    previous = None
    for i in latlong:

        x = distance.distance(clientcords, i)
        previous = x
        print("X",x," prev:",previous)
        if x < previous:
            print(previous)
            previous = x

    clientcords = ()
    closetsdriver = i

















