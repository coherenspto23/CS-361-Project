import json
import os
from datetime import datetime

def save_game(player, world, filename=None):
    """Save current state of the game to a JSON file"""
    # Create a dictionary to hold the game state
    if not os.path.exists("data/saves"):
        os.makedirs("data/saves")
    #save data
    save_data = {
        'timestamp': datetime.now().isoformat(),
        'player': {
            'name': player.name,
            'occupation': player.occupation,
            'background': player.background,
            'level': player.level,
            
            # Resources
            'health': player.health,
            'max_health': player.max_health,
            'mana': player.mana,
            'max_mana': player.max_mana,
            'stamina': player.stamina,
            'max_stamina': player.max_stamina,
            
            # Stats
            'strength': player.strength,
            'magic': player.magic,
            'agility': player.agility,
            'defense': player.defense,
            'luck': player.luck,
            
            # Possible future additions:
            # 'experience': player.experience,
            # 'inventory': player.inventory,
        },
        'world': {
            'current_location': world.current_location
        }
    }

    # save to file
    save_file_path = f'data/saves/{filename}.json'

    try:
        with open(save_file_path, 'w') as f:
            json.dump(save_data, f, indent=2)
            print(f"Game saved successfully to {save_file_path}") # Success message for testing will be changed later
    except Exception as e:
        print(f"Error saving game: {e}")
    
def load_game(filename):
    """Load game from a JSON file and return player to world state """

    save_file_path = f'data/saves/{filename}.json'
    if not os.path.exists(save_file_path):
        print(f"Error: Save file '{save_file_path}' not found!")
        return None, None # Return None for both player and world if loading fails
    try:
        with open(save_file_path, 'r') as f:
            save_data = json.load(f)
        # Create player and world objects based on loaded data
        from character import Character
        from world import World
        player_data = save_data['player']

        # Load player data
        player = Character(
            name=player_data['name'],
            occupation=player_data['occupation'],
            background=player_data['background']
        )
        # load player stats
        player.level = player_data['level']
        player.health = player_data['health']
        player.max_health = player_data['max_health']
        player.mana = player_data['mana']
        player.max_mana = player_data['max_mana']
        player.stamina = player_data['stamina']
        player.max_stamina = player_data['max_stamina']
        player.strength = player_data['strength']
        player.magic = player_data['magic']
        player.agility = player_data['agility']
        player.defense = player_data['defense']
        player.luck = player_data['luck']
        
        # Load world data
        world = World()
        world.current_location = save_data['world']['current_location']
        #
        print(f"Game loaded successfully from {save_file_path}") 
        return player, world

    except Exception as e:
        print(f"Error loading game: {e}")
        return None, None
        
def list_saves():
    """List all available save files"""
    
    saves_dir = 'data/saves'
    
    if not os.path.exists(saves_dir):
        print("No save files found.")
        return []
    
    save_files = [f for f in os.listdir(saves_dir) if f.endswith('.json')]
    
    if not save_files:
        print("No save files found.")
        return []
    
    print("\n=== Available Saves ===")
    for i, save_file in enumerate(save_files, 1):
        save_name = save_file.replace('.json', '')
        save_path = os.path.join(saves_dir, save_file)
        
        try:
            with open(save_path, 'r') as f:
                data = json.load(f)
            
            player_name = data['player']['name']
            level = data['player']['level']
            location = data['world']['current_location']
            timestamp = data.get('timestamp', 'Unknown')
            
            print(f"{i}. {save_name}")
            print(f"   Character: {player_name} (Level {level})")
            print(f"   Location: {location}")
            print(f"   Saved: {timestamp[:19]}")  # Show date without milliseconds
            print()
        except:
            print(f"{i}. {save_name} (corrupted)")
    
    return save_files


# Test functions
if __name__ == "__main__":
    print("Save/Load system test")
    list_saves()