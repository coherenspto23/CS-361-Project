import os
import json

class World:
    """Class to manage the game world, 
    including its locations, descriptions and moving around it"""
    def __init__ (self, location_file="data/locations.json"):
        self.locations_file = location_file         # Path to the JSON file containing location data
        self.locations = self.load_locations()      # Load locations from the JSON file
        self.current_location = None                # Current location of the player, will be set when the game starts
    def load_locations(self):
        """Load the locations from the JSON file"""
        if not os.path.exists(self.locations_file): # Check if the file exists
            print(f"Error: {self.locations_file} not found!")
            return {}
        with open(self.locations_file, "r") as f:   # Open the file and load the JSON data
            return json.load(f)
    
    def set_starting_loc(self, location_name):
        """Set starting location for player"""
        if location_name in self.locations:
            self.current_location = location_name
            self.describe_location()
        else:
            print(f"Error: Location '{location_name}' not found in world data!")
        
    def get_current_location(self):
        """Return data for current location of player"""
        if self.current_location:
            return self.locations[self.current_location] # get the data for the current location
        else:
            print("Error: Cannot get current location") 
            return None
    def describe_location(self):
        """Print location description and available exits"""
        location = self.get_current_location()
        if not location:                                # Test to ensure start location is set and valid
            print("Error: Where am I? No location data found!")
            return 
        
        print(f"\n" + "="*50)
        print(f" {location['name']}")
        print("="*50)
        print(location['description'])

        # Show connections, items, and NPCs from .JSON data
        exits = []
        for direction in ["north", "south", "east", "west"]:
            destination = location["connections"].get(direction)
            if destination is not None:
                exits.append(direction.capitalize())
        # Display exits, items, and NPCs
        print(f"\nExits: {', '.join(exits)}")

        if location.get("items"):
            print(f"Items here: {', '.join(location['items'])}") # Will probably change this as it makes no sense 
                                                                 # to display indvidual itmes for the most part
        if location.get("npcs"):
            print(f"People here: {', '.join(location['npcs'])}")
        
        if location.get("enemies"):
            print(f"Enemies here: {', '.join(location['enemies'])}")

        print(f"{'='*50}\n")
    def move(self, direction):
        """Move the player in the specified direction if possible"""
        # Define a mapping for shorthand directions
        direction = direction.lower()
        direction_map = {
            "n": "north",
            "s": "south",
            "e": "east",
            "w": "west"
        }
        if direction in direction_map:
            direction = direction_map[direction]
        # Validate the direction
        if direction not in ["north", "south", "east", "west"]:
            print("Invalid direction! Use N, S, E, W or the full direction name.")
            return
        # Get the current location data
        location = self.get_current_location()
        next_location = location['connections'].get(direction)
        if next_location is None:                                 # Check if location is blocked (WILL BE NULL IN JSON)
            print(f"You can't go {direction.capitalize()} from here! It is blocked.")
            return False
        # Move to the next location
        self.current_location = next_location
        print(f"You have travled {direction.capitalize()} to {self.locations[next_location]['name']}")
        self.describe_location()
        return True