#MATH adventure text based game on a story!

# ——— ALL IMPORTS ——— #
import time
import random

# ——— ALL FIXED DEF AND VARIABLES ——— #
splash_notes = [
            "fixing turtles",
            "adding jokes",
            "making NPC",
            "feeding villagers",
            "sharpening swords",
            "building bridges",
            "plucking flowers",
            "collecting coins",
            "drawing maps",
            "rolling dice"]

player_stats = {
        "name": player_name,
        "vitality": 100, #hp
        "dexterity": 5,  #crit chance/accuracy
        "strength":  5,  #dmg multipler
        "agility": 5,  #turn order"(when > oppnt you frst)
        "luck": 1,  #loot chance
        "wisdom": 1,  #heal rate/item buff
        "money": 10,  #$$$$$$$$$$
        }

take_dmg = player_stats["vitality"]-(enemy_dmg * random.uniform(1.8,2.3)/armour_points

dmg_delt = enemy_hp

def loading_effect_with_splash_effect(n):
    for _ in range(n):
        splashN = random.choice(splash_notes)
        time.sleep(0.3)
        print(splashN + "\n. . .")


# ——— GAME CODE ——— #
game_start = input("do you want to start the game? = ")
game_start = game_start.strip().lower()

if game_start in ("y", "yes"):
    time.sleep(0.5)
    print("STARTING. . .")
    loading_effect_with_splash_effect(5)
    player_name = input("what is the name if your player? =")
