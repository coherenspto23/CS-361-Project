class Character:
    def __init__(self, name, occupation, background):
        self.name = name
        self.occupation = occupation
        self.background = background
        self.level = 1

        # attributes
        self.health = 100
        self.mana = 40
        self.stamina = 75

        # Initialize stats
        self.strength = 5
        self.magic = 5
        self.agility = 5
        self.defense = 5
        self.luck = 5
        
        # Stats based on occupation
        if occupation.lower() == "warrior":
            self.health += 40
            self.stamina += 25
            self.mana -= 30
            self.strength = 8
            self.magic = 2
            self.defense += 2
            self.agility -= 1
        elif occupation.lower() == "mage":
            self.health -= 30
            self.stamina += 15
            self.mana += 60
            self.strength = 2
            self.magic = 9
            self.defense -= 3
            self.agility += 1
        elif occupation.lower() == "rogue":
            self.health -= 20
            self.stamina += 30
            self.mana -= 10
            self.strength -= 1
            self.magic -= 2
            self.agility += 3

        # Stats based on background
        if background.lower() == "noble":
            self.luck += 3
            self.defense += 1
        elif background.lower() == "soldier":
            self.strength += 2
            self.health += 10
            self.defense += 1
        elif background.lower() == "scholar":
            self.magic += 2
            self.mana += 10
            self.luck += 1
        elif background.lower() == "commoner":
            self.stamina += 5
            self.health += 5
            self.strength += 1
            self.agility += 1
        elif background.lower() == "merchant":
            self.luck += 3
            self.defense += 1
        elif background.lower() == "outlaw":
            self.agility += 2
            self.stamina += 10
            self.luck += 1
            self.defense -= 1
        
        # Set max values
        self.max_health = self.health
        self.max_mana = self.mana
        self.max_stamina = self.stamina
    
    def display_stats(self):
        """Display character stats"""
        print(f"\n{'='*50}")
        print(f"{self.name} - Level {self.level} {self.occupation}")
        print(f"Background: {self.background}")
        print(f"{'='*50}")
        print(f"Health:  {self.health}/{self.max_health}")
        print(f"Mana:    {self.mana}/{self.max_mana}")
        print(f"Stamina: {self.stamina}/{self.max_stamina}")
        print(f"\nStrength: {self.strength}")
        print(f"Magic:    {self.magic}")
        print(f"Agility:  {self.agility}")
        print(f"Defense:  {self.defense}")
        print(f"Luck:     {self.luck}")
        print(f"{'='*50}")


def create_character():
    """Simple character creation"""
    print("=== Character Creation ===")
    
    # Get name
    name = input("\nEnter your name: ").strip()
    while not name:
        print("Name cannot be empty!")
        name = input("Enter your name: ").strip()
    
    # Choose occupation
    print("\nChoose your occupation:")
    print("1. Warrior")
    print("2. Mage")
    print("3. Rogue")
    
    occupations = {"1": "Warrior", "2": "Mage", "3": "Rogue"}
    occupation_choice = input("Enter choice (1-3): ").strip()
    
    while occupation_choice not in occupations:
        print("Invalid! Choose 1, 2, or 3.")
        occupation_choice = input("Enter choice (1-3): ").strip()
    
    occupation = occupations[occupation_choice]
    
    # Choose background
    print("\nChoose your background:")
    print("1. Noble")
    print("2. Soldier")
    print("3. Scholar")
    print("4. Commoner")
    print("5. Merchant")
    print("6. Outlaw")
    
    backgrounds = {
        "1": "Noble",
        "2": "Soldier",
        "3": "Scholar",
        "4": "Commoner",
        "5": "Merchant",
        "6": "Outlaw"
    }
    
    background_choice = input("Enter choice (1-6): ").strip()
    
    while background_choice not in backgrounds:
        print("Invalid! Choose 1-6.")
        background_choice = input("Enter choice (1-6): ").strip()
    
    background = backgrounds[background_choice]
    
    # Create character
    player = Character(name, occupation, background)
    
    print(f"\nWelcome, {player.name} the {player.occupation}!")
    player.display_stats()
    
    return player


if __name__ == "__main__":
    test_character = create_character()
    print("\nCharacter created successfully!")