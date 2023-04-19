"""

This code implements an adventure game where the player is presented with options 
and can explore different areas, 
battle enemies, and complete quests.

NAME: jie Chen
SEMESTER: 2023 Spring
"""
import time


def print_pause(message):
    """
    The print_pause function is used to
    print a message with a 2 second delay.
    """
    print(message)
    time.sleep(2)


def intro():
    """
    The intro function is used to introduce the game
    and set the scene for the player.
    """
    print_pause("Welcome to the adventure game!")
    print_pause("You find yourself in a dark forest.")
    print_pause("You can see a path leading to a castle in the distance.")


def get_choice():
    """
    The get_choice function is used to get the player's input and validate
    it to ensure that it is a valid choice.
    """
    while True:
        try:
            choice = input("Enter 1 to follow the path to the castle.\n"
                           "Enter 2 to explore the forest.\n"
                           "Enter help for a list of available commands.\n")

            if choice in ['1', '2']:
                break
            else:
                print_pause("Invalid choice. Please try again.")
        except ValueError:
            print_pause("Invalid input. Please enter a number.")
    return choice


def follow_path(enemy):
    """
    The follow_path function is used to
    simulate the player following the path to the castle.
    """
    print_pause("You follow the path to the castle.")
    print_pause("As you get closer, you see a guard at the gate.")
    print_pause("The guard asks for your name and business.")
    name = input("What is your name?\n")
    print_pause(f"The guard nods and lets you enter the castle, {name}.")
    castle(enemy)


def combat(player_hp, player_attack, enemy_hp, enemy_attack):
    """
    The combat function is used to simulate a battle
    between the player and an enemy.
    """
    print_pause("A wild enemy appears!")
    while player_hp > 0 and enemy_hp > 0:
        print_pause(f"Player HP: {player_hp}")
        print_pause(f"Enemy HP: {enemy_hp}")
        choice = input("Enter 1 to attack.\n"
                       "Enter 2 to defend.\n")
        if choice == '1':
            print_pause("Player attacks the enemy!")
            enemy_hp -= player_attack
            if enemy_hp <= 0:
                break
            print_pause("Enemy counterattacks!")
            player_hp -= enemy_attack
        elif choice == '2':
            print_pause("Player defends!")
            player_hp -= enemy_attack // 2
        else:
            print_pause("Invalid choice. Please try again.")
    if player_hp > 0:
        print_pause("Player defeats the enemy!")
        return True
    else:
        print_pause("Player is defeated...")
        return False


def explore_forest():
    """
    The explore_forest function is used to guide the player
    through the forest.
    """
    print_pause("You wander through the forest.")
    print_pause("You come across a clearing with a pond.")
    print_pause("You notice a sword lying on the ground near the pond.")
    choice = input("Enter 1 to take the sword.\n"
                   "Enter 2 to leave it.\n")
    if choice == '1':
        print_pause("You take the sword and continue through the forest.")
    elif choice == '2':
        print_pause("You leave the sword and continue through the forest.")
    else:
        print_pause("Invalid choice. Please try again.")
        explore_forest()
    forest()


def castle(enemy):
    """ The castle function is used to guide the player through the castle. """
    print_pause("You are inside the castle.")
    print_pause("You see a knight in shining armor walking towards you.")
    print_pause("The knight greets you and offers to take you on a tour.")
    choice = input("Enter 1 to accept the offer.\n"
                   "Enter 2 to decline and leave the castle.\n")
    if choice == '1':
        print_pause(
            "The knight shows you the throne room, the banquet hall, and the armory.")
        print_pause("He also gives you a map of the kingdom.")
        print_pause(
            "You leave the castle feeling more knowledgeable about the land.")
        if enemy is not None:
            if combat(10, 2, enemy['hp'], enemy['attack']):
                print_pause(f"You found a {enemy['loot']}!")
            else:
                print_pause("You didn't find any loot.")
    elif choice == '2':
        print_pause("You decline the offer and leave the castle.")
    else:
        print_pause("Invalid choice. Please try again.")
        castle(enemy)


def forest():
    """ The forest function is used to guide the player through the forest. """
    print_pause("You are back in the forest.")
    print_pause("You notice a signpost pointing to different directions.")
    choice = input("Enter 1 to follow the path to the village.\n"
                   "Enter 2 to climb the mountain.\n"
                   "Enter 3 to cross the desert.\n")
    if choice == '1':
        village()
    elif choice == '2':
        mountain()
    elif choice == '3':
        desert()
    else:
        print_pause("Invalid choice. Please try again.")
        forest()


def village():
    """
    The village function is used to guide the player through the village.
    """
    print_pause("You arrive at the village.")
    print_pause("The villagers greet you warmly and offer you a place to stay.")
    choice = input("Enter 1 to accept the offer.\n"
                   "Enter 2 to decline and leave the village.\n")
    if choice == '1':
        print_pause("You stay with the villagers for a night.")
        print_pause("They share stories and songs with you.")
        print_pause("The next morning, the village elder asks for your help.")
        print_pause("The village has been plagued by a group of bandits.")
        print_pause("The elder asks you to help drive them away.")
        bandits_choice = input("Enter 1 to accept the quest.\n"
                               "Enter 2 to decline and leave the village.\n")
        if bandits_choice == '1':
            print_pause("You agree to help the village.")
            print_pause(
                "The villagers give you a map of the bandits' hideout.")
            print_pause("You travel to the hideout and confront the bandits.")
            print_pause("After a fierce battle, you emerge victorious.")
            print_pause(
                "The village thanks you and rewards you with a rare item.")
            print_pause("You leave the village feeling proud and fulfilled.")
        elif bandits_choice == '2':
            print_pause("You decline the quest and leave the village.")
        else:
            print_pause("Invalid choice. Please try again.")
            village()
    elif choice == '2':
        print_pause("You decline the offer and leave the village.")
    else:
        print_pause("Invalid choice. Please try again.")
        village()


def mountain():
    """
    The mountain function is used to guide the player through the mountain.
    """
    print_pause("You start climbing the mountain.")
    print_pause("It's a steep climb but you keep going.")
    print_pause("After a few hours, you reach the top.")
    print_pause("You can see the entire kingdom from up here.")
    print_pause("You feel a sense of accomplishment.")
    print_pause("You climb down the mountain and return to the forest.")
    forest()


def desert():
    """ The desert function is used to guide the player through the desert. """
    print_pause("You start walking across the desert.")
    print_pause("The sun is beating down on you and you're getting thirsty.")
    print_pause("After a while, you see an oasis in the distance.")
    choice = input("Enter 1 to go to the oasis.\n"
                   "Enter 2 to keep walking.\n")
    if choice == '1':
        print_pause("You go to the oasis and quench your thirst.")
        print_pause("You also find a treasure chest filled with gold.")
        print_pause("You leave the oasis feeling richer and more refreshed.")
        forest()
    elif choice == '2':
        print_pause("You keep walking.")
        print_pause("After a few more hours, you start feeling dizzy.")
        print_pause("You collapse on the sand.")
        print_pause("You wake up in a tent.")
        print_pause("A group of nomads have rescued you.")
        print_pause("They nurse you back to health.")
        print_pause("You thank them and leave the desert feeling grateful.")
        forest()
    else:
        print_pause("Invalid choice. Please try again.")
        desert()


def play_game():
    """ The play_game function is used to start the game. """
    intro()
    choice = get_choice()
    if choice == '1':
        enemy = {'hp': 5, 'attack': 1, 'loot': 'potion'}
        follow_path(enemy)
    elif choice == '2':
        explore_forest()
    else:
        print_pause("Invalid choice. Please try again.")
        play_game()


play_game()
