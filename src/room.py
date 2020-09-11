# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description):
      self.name = name
      self.description = description
      self.n_to = False
      self.s_to = False
      self.e_to = False
      self.w_to = False
      self.inventory = []
    def add_item(self, item):
      self.inventory.append(item)
    def remove_item(self, item):
      self.inventory.remove(item)
    def __str__(self):
      return f'{self.name}'