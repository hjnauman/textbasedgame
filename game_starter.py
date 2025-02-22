import random

# Food values
food = random.randint(0,2)
CANDY = 0
STEAK = 1
POTION = 2
CANDY_RESTORE = 10
STEAK_RESTORE = 20
POTION_RESTORE = 40

# Creature values
BUNNY = 0
DWARF = 1
TROLL = 2
WYVERN = 3
GAMBLER = 4
BUNNY_DAMAGE = 5
DWARF_DAMAGE = 10
TROLL_DAMAGE = 20
WYVERN_DAMAGE = 25
GAMBLER_DAMAGE = random.randint(0,35)

# Misc values
TUITION = 50
BEER = 10
max_gold = 95

def print_status(gold: int, health: int):
    '''
    This function print's the players current status.
    
    Params
    ------
    gold : int
        The current amount of gold the user has.
    health : int
        The users current health.
    '''
    if gold > 2 * health:
        print('\nYou are rich with ' + str(gold) + ' gold, but your health is only ' + str(health) + '\n')
    elif health > 2 * gold:
        print('\nYou are strong with ' + str(health) + ' health, but you only have ' + str(gold) + ' gold\n')
    else:
        print('\n Your health is ' + str(health) + ' and you have ' + str(gold) + ' gold\n')
        
def find_treasure(max_gold: int) -> int:
    '''
    This function calculates how much treasure is found by generating a random gold amount between 1 and the max number of gold coins.
    
    Params
    ------
    max_gold : int
        The maximum amount of gold possible to find.
    
    Returns
    -------
    int
        The actual amount of gold the user found.
    ''' 
    gold = random.randint(1, max_gold)
    
    if gold < max_gold / 2:
        print('\nYou find ' + str(gold) + ' gold pieces on the floor.\n')
    else:
        print('\nYou find a huge mound of ' + str(gold) + ' gold pieces!\n')
    
    return gold
    
def eat_food(food: int, health: int):
    '''
    This function allows the player to eat one of the optional food items which will update their health and print a message.
    
    Params
    ------
    food : int
        The food item being chosen. This number corresponds to the global variables we've created, however, there is a base case if the user attempts to eat
        nothing.
    health : int
        The player's current health prior to eating.
    '''
    # Check which food the user is eating then update their health and print a message about what they ate
    if food == CANDY:
        health += CANDY_RESTORE
        print('\nYou find a half eaten energy bar on the floor which restores your health by ' + str(CANDY_RESTORE) + '\n')
        
    elif food == STEAK:
        health += STEAK_RESTORE
        print('\nYou find a warm and juicy steak on the table which restores your health by ' + str(STEAK_RESTORE) + '\n')
        
    elif food == POTION:
        health += POTION_RESTORE
        print('\nYou find a green glowing potion on a shelf which restores your health by ' + str(POTION_RESTORE) + '\n')
        
    else:
        print('\nYour stomach is rumbling, but there is nothing to eat\n')
        
    if health > 100:
        health = 100
        
def fight_battle(creature: int):
    '''
    This function simulates battle with one of the optional creatures. A damage value will be generated based on each creatures max damage and a message will
    be given to the user regarding their battle.
    
    Params
    ------
    creature : int
        The creature that you are fighting. This number corresponds to the global variables we've created, however, there is a base case if the user attempts
        to fight nothing.
        
    Returns
    -------
    int
        The damage dealt to the player during the battle.
    ''' 
    damage = 0
    
    
    if creature == BUNNY:
        damage = random.randint(1, BUNNY_DAMAGE)
        print('\nYou trip over a cute bunny and do ' + str(damage) + ' damage to your health.\n')
        
    elif creature == DWARF:
        damage = random.randint(1, DWARF_DAMAGE)
        print('\nA drunken dwarf hits you with a beer mug and does ' + str(damage) + ' damage to your health.\n')
    
    elif creature == TROLL:
        damage = random.randint(1, TROLL_DAMAGE)
        print('\nAn angry troll kicks you in the rear and does ' + str(damage) + ' damage to your health.\n')
        
    else:
        print('\nIt is ghostly quiet here, you must be alone\n')
        
    return damage
    
def get_direction() -> str:
    '''
    This function gets what direction the user would like to travel.
    
    Returns
    -------
    str
        User choice of direction between one of the following values (N, S, E, W, NE, NW, SE, SW)
    ''' 
    optional_directions = ['N', 'S', 'E', 'W', 'NE', 'NW', 'SE', 'SW']
    direction = input('\nWhat direction would you like to go? (N,NE,NW,S,SE,SW): ').upper()
    
    while direction not in optional_directions:
        print('Sorry, you can not go that way...\n')
        direction = input('What direction would you like to go? (N,NE,NW,S,SE,SW): ').upper()
        
    return direction
    
def game_exit(gold: int, health: int):
    print('\n------------------------------------------------------------')
    print('You crawl out of the cave and blink your eyes to')
    print('adjust to the bright sunshine. Congratulations,')
    print('you made it out of the cave with ' + str(health) + 'health!')
    
    if gold >= TUITION:
        print('\nYou empty your pockets and discover ' + str(gold) + 'gold coins.')
        print('This will pay for the tuition next semester!!!')
        
    elif gold >= BEER:
        print('\nYou notice that you have ' + str(gold) + ' gold coins in your pocket.')
        print('This will pay for beer and pizza next semester!!!')
        
    else:
        print('\nYou check your pocket and find ' + str(gold) + ' gold coins.')
        print('Exploring caves sure is a hard way to make money!!!')
        
    exit()
    
def room_1(gold: int, health: int):
    '''
    This function visits the first room in the game and starts off the story.
    
    Params
    ------
    gold : int
        The amount of gold the player currently has.
    health : int
        The amount of gold the player currently has.
    ''' 
    print('\n------------------------------------------------------------')
    print('You just stumbled into a hold in the ground. When you')
    print('shake off the dirt and leaves you realize you are in')
    print('the entrance to a cave that looks man made. As you')
    print('take a look around, you decide it might be fun to explore.\n')
    
    # Sequence 1
    direction = get_direction()
    
    
    if direction == 'N' or 'S':
        fight_battle(creature)
    elif direction == 'E':
        eat_food(food, health)
    elif direction == 'NE' or 'SE':
        eat_food(food, health)
    elif direction == 'SW' or 'NW':
        fight_battle(creature)
    else:
        eat_food(food, health)
    
    print_status(gold, health)
    
    # Sequence 2
    direction = get_direction()
    if direction == 'N' or 'S':
        gold = find_treasure(max_gold)
    elif direction == 'E':
        eat_food(food, health)
    elif direction == 'NE' or 'SE':
        fight_battle(creature)
    elif direction == 'SW' or 'NW':
        fight_battle(creature)
    else:
        eat_food(food, health)
    
    print_status(gold, health)

 # Sequence 2
    direction = get_direction()
    if direction == 'N' or 'S':
        creature = fight_battle(creature)
    elif direction == 'E':
        gold = find_treasure(max_gold)
    elif direction == 'NE' or 'SE':
        eat_food(food, health)
    elif direction == 'SW' or 'NW':
        fight_battle(creature)
    else:
        eat_food(food, health)
    
    print_status(gold, health)
    
def room_2(gold: int, health: int):
    '''
    This function visits the second room in the game.
    
    Params
    ------
    gold : int
        The amount of gold the player currently has.
    health : int
        The amount of gold the player currently has.
    ''' 
    print('\n------------------------------------------------------------')
    print('You have entered the throne room. In the middle')
    print('of the room there is a giant wooden throne with')
    print('intricate carvings. As you take a closer look at the')
    print('carvings, you see that they show trolls chasing humans.')
    print('Hmmm, maybe this is not a great place to stop for a rest.\n')
    
    # Add your own code here
    
    print_status(gold, health)
    
def room_3(gold: int, health: int):
    '''
    This function visits the third room in the game.
    
    Params
    ------
    gold : int
        The amount of gold the player currently has.
    health : int
        The amount of gold the player currently has.
    ''' 
    print('\n------------------------------------------------------------')
    print('You have entered an abandoned pub. There are piles')
    print('of dirty dishes and empty beer mugs all over the place.')
    print('You hear someone coming and duck behind a table to hide.\n')
    
    # Add your own code here
    
    print_status(gold, health)
    
def room_4(gold: int, health: int):
    '''
    This function visits the fourth room in the game.
    
    Params
    ------
    gold : int
        The amount of gold the player currently has.
    health : int
        The amount of gold the player currently has.
    ''' 
    print('\n------------------------------------------------------------')
    print('You have entered a huge storage room filled with empty boxes.')
    print('Looking at the side of one box, you see \'ACME troll food\'.')
    print('You better get out of here before you end up on the menu.\n')
    
    # Add your own code here
    
    print_status(gold, health)
    
# Add additional room functions following these functions

if __name__ == '__main__':
    # Initialize player values
    gold = 0
    health = 100
    room_1(gold, health)