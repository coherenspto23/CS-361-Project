from character import create_character
from world import World
from save_load import save_game, load_game, list_saves
### In development will ADD RICH LIBRARY LATER FOR BETTER DISPLAY

def intro_to_game():

    print("="*50)
    print("Hello adventurer! Welcome to Northumbria, a simple text-based RPG set in a medieval world.")
    print("\n This is a small intro that will give you a quick run down on the basics of palying the game")
    print("\n First you will create your character than be unleasehd into the world of Northumbria.")
    print("\n Below is a list of basic commands you will need to be able to play the game")
    print("\n Commands:")
    print("To move - north/n, south/s, east/e, west/w")
    print("To save or load - save")
    print("To get help - help/h")
    print("="*50)




def main():
    """Main game entry point"""
    print("="*50)
    print("  WELCOME TO NORTHUMBRIA")
    print("="*50)
    intro_to_game()
    print("\n1. New Game")
    print("2. Load Game")
    print("3. Quit")
    
    choice = input("\nChoose (1-3): ").strip()
    
    if choice == "1":
        # New game
        player = create_character()
        world = World('data/locations.json')
        world.set_starting_loc('maevr_village')
        
    elif choice == "2":
        # Load game
        list_saves()
        save_name = input("\nEnter save name (or 'cancel'): ").strip()
        
        if save_name.lower() == 'cancel' or not save_name:
            print("Load cancelled.")
            return
        
        player, world = load_game(save_name)
        
        if player is None:
            print("Load failed. Returning to menu...")
            return
        else:
            world.describe_location()
    
    elif choice == "3":
        print("Goodbye!")
        return
    
    else:
        print("Invalid choice!")
        return
    
    # Start game loop
    game_loop(player, world)


def game_loop(player, world):
    """Main game loop with save functionality"""
    print(f"\n{player.name} begins exploring...")
    
    while True:
        command = input("\n> ").lower().strip()
        
        if command in ['quit', 'exit', 'q']:
            print("\nDo you want to save before quitting?")
            save_choice = input("(yes/no): ").lower().strip()
            
            if save_choice in ['yes', 'y']:
                save_name = input("Save name (default: save1): ").strip() or "save1"
                save_game(player, world, save_name)
            
            print("Thanks for playing!")
            break
        
        elif command == 'save':
            save_name = input("Save name (default: save1): ").strip() or "save1"
            save_game(player, world, save_name)
        
        elif command in ['north', 'south', 'east', 'west', 'n', 's', 'e', 'w']:
            world.move(command)
        
        #elif command in ['look', 'l']:     
         #   world.look()
        
        elif command in ['help', 'h', '?']:
            print("\nCommands:")
            print("  north/n, south/s, east/e, west/w - Move")
            #print("  look/l - Look around") Will be added later just putting it here for now
            print("  stats - Show character stats")
            print("  save - Save game")
            print("  help/h - Show this help") 
            print("  quit/q - Quit game")
        
        elif command == 'stats':
            player.display_stats()
        
        else:
            print("Unknown command. Type 'help' for commands.")


if __name__ == "__main__":
    main()