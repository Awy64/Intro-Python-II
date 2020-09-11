# Write a class to hold player information, e.g. what room they are in
# currently.
import textwrap

class Player():
    def __init__(self, loc):
      self.loc = loc
      self.inventory = []
    def add_item(self, item):
      self.inventory.append(item)
      self.loc.inventory.remove(item)
    def remove_item(self, item):
      self.inventory.remove(item)
      self.loc.inventory.append(item)
    def player_items(self):
      print([str(i) for i in self.inventory])
    def room_items(self):
      print([str(i) for i in self.loc.inventory])
    def __str__(self):
      return f"{self.loc.name} {self.loc.description}"
    def move_to(self, loc):
      self.loc = loc