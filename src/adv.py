import textwrap
from room import Room
from player import Player
import os
import time
from item import Item
import re


# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                    "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}

# declare all items

item = {
    'candle': Item("candle", "A dim candle to light the way"),

    'bottle': Item('bottle', "A bottle"),

    'diamond': Item('diamond', "So there is treasue in here.")
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

# Add Items to room

room['outside'].add_item(item['candle'])
room['treasure'].add_item(item['diamond'])
room['overlook'].add_item(item['bottle'])

# Main
#

# Make a new player object that is currently in the 'outside' room.
tom = Player(room['outside'])
# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

def clear():
    return os.system('cls' if os.name == 'nt' else 'clear')

while True:
    clear()
    print(textwrap.fill(str(tom), width=70))
    tom.room_items()
    inputs = input("Please select north 'n' south 's' east 'e'  west 'w' quit 'q' ")
    if (len(inputs) == 1):
      if inputs == 'q': ## quit
        break
      elif inputs == 'i': ## inventory
        tom.player_items()
        input('Press enter to continue')
      else:
        print('please choose a action')
        input('Press enter to continue')
        continue
    elif (len(re.findall(r'\w+', inputs)) == 2): 
      global v
      global o 
      v,o = inputs.split()
    else:
      continue
    ## begin move
    if v == 'move':
      if o == 'n':
        if tom.loc.n_to == False:
          print('you cant go this way')
          input('Press enter to continue')
        else:
          tom.move_to(tom.loc.n_to)
          clear()
      elif o == 'e':
        if tom.loc.e_to == False:
          print('you cant go this way')
          input('Press enter to continue')
        else:
          tom.move_to(tom.loc.e_to)
          clear()
      elif o == 's':
        if tom.loc.s_to == False:
          print('you cant go this way')
          input('Press enter to continue')
        else:
          tom.move_to(tom.loc.s_to)
          clear()
      elif o == 'w':
        if tom.loc.w_to == False:
          print('you cant go this way')
          input('Press enter to continue')
        else:
          tom.move_to(tom.loc.w_to)
          clear()
      else:
        print("please select a direction")
        input('Press enter to continue')
    ## end move
    ## begin take
    elif v == 'take': 
      if (o in item and item[o] in tom.loc.inventory):
        tom.add_item(item[o])
        print(f'{o} added to inventory')
        input('Press enter to continue')
      else:
        print('item not found')
        input('Press enter to continue')
    ## end take
    elif v == 'drop':
      if (o in item and item[o] in tom.inventory):
        tom.remove_item(item[o])
        print(f'{o} removed to inventory')
        input('Press enter to continue')
      else:
        print('item not found')
        input('Press enter to continue')



