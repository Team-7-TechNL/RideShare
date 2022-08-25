from typing import Tuple
import folium

def Mapmain(cords):

    #sets up the map to 0,0
    if cords != (0,0):
        StartPos = cords
        Zoom = 19.3
    else:
        Zoom = 3
        StartPos = (0, 0)



    # Cords could be stored in a DataBase
    cords = [(47.51044931589316, -52.92471902671029),
             (47.50997182304524, -52.924989780304585),
             (47.5117538621506, -52.92535888029291),
             (47.51239826716989, -52.92605581737727),
             (47.5119085248456, -52.92771487525117),
             (47.51798725653911, -52.933987077831056),
             (47.52029535370516, -52.93654879275768)]

    # Creates the map
    my_map = folium.Map(location=StartPos, zoom_start=Zoom,min_zoom=0,max_zoom=19.3)

    from Distchecker import distchecker, closetsdriver
    if closetsdriver != 0:
        folium.CircleMarker(location=closetsdriver, radius=50, popup="Closet Driver", color="#3186cc",
                            fill=True,
                            fill_color="#3186cc", ).add_to(my_map)


    # Adds markers to the map
    for i in cords:
        icon = folium.Icon(color='white', icon='car', icon_color="black", prefix='fa')
        folium.Marker(i, icon=icon).add_to(my_map)



    # Displays the map

    my_map.save('aee.html')