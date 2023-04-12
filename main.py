# Imports.
import time, threading

# Modules.
from modules.map import Map
from modules.beacon import Beacon
from modules.geoloc import Geolocator

# Global variables.
threat_map = Map()
geolocator = Geolocator()

# Todo: implement collection
storage = {}
ports = {
    5120 : "SSH",
    5180 : "HTTP"
}

def beacon(port):
    data = None
    new_beacon = Beacon(port=port)
    while 1:
        
        new_beacon.listen()

        new_data = new_beacon.get_data()
        
        ip = list(new_data.keys())[-1].split(":")[0]
        coordinates = geolocator.get_location( ip ) 
                
        threat_map.generate_marker(coordinates, name= ports[int( port )] )
        threat_map.generate_map()

    return 0

def main():
    threads = []

    for port in [5120, 5180]:
        time.sleep(5 / 10)

        thread = threading.Thread(target=beacon, args=(port,))
        thread.start()
        threads.append(thread)

        

    for thread in threads:
        thread.join()

if __name__ == "__main__":
    main()