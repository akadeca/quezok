class Item:
    """A Item is an item which can be consumed."""

    def __init__(self, name, count, verb, act):
        self.name = name
        self.count = count
        self.verb = verb
        self.act = act

    def use(self):
        if self.count <= 0:
            print("You don't have any more of those.")
        else:
            print('You ' + self.verb + ' the ' + self.name + '.')
            self.act()
            self.count -= 1
