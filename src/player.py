# Write a class to hold player information, e.g. what room they are in
# currently.
import textwrap

class Player():
    def __init__(self, loc):
      self.loc = loc
    def __str__(self):
      return f"{self.loc.name} {self.loc.description}"
    def move_to(self, loc):
      self.loc = loc