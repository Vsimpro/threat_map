import folium

class Map:
    def __init__(self):
        self.map = folium.Map(location=[50,30], zoom_start=3)
        self.generate_map()

    # Save and generate a new map.html
    def generate_map(self):
        self.map.save("map.html")

    # Add markers.
    def generate_marker(self, coordinates, name=""):
        if len(coordinates) != 2:
            print("marker coordinates must be [lat, lon]")
            return 1
        
        # Bit hard to read, basically adds a new marker to desired loc
        folium.Marker(
            [coordinates[0], coordinates[1]], 
            icon=folium.Icon(
                color='red', 
                icon='fire'
            ), 
            popup='(0, 0)',
            tooltip=name)\
        .add_to(self.map)