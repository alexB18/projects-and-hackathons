from RadiusMap import *

if __name__ == "__main__":

    killswitch = False

    while killswitch == False:
        types = []
        radius = 0

        address = input("Please enter your starting location (enter q to quit): ")
        if address == 'q':
            killswitch = True

        radius_string = input("Please enter search radius in meters (enter q to quit): ")
        if radius_string == 'q':
            killswitch = True
        else:
            radius = int(radius_string)

        gettingtypes = True
        while(gettingtypes):
            type = input("Please enter which types of places you'd like to visit on your run (enter q to quit/d " +
                         "when you're done entering them): ")
            if type == 'q':
                killswitch = True
            elif type == 'd':
                gettingtypes = False
            else:
                types.append(type)

        print("")
        Map = RadiusMap(address, radius, types)
        Map.generate_start_geo()
        Map.generate_destinations_dataframe()
        Map.generate_random_route(Map.possible_route_coordinates, 5)
        print("")
        print(Map.current_route)
        print("")
        Map.plot_route_from_geolocations(Map.current_route, 'walking')
        print("")


        keep_going = input("Keep Going? (y/n): ")
        if keep_going == 'n':
            killswitch = True