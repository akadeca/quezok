#! /usr/bin/env python
# quezok.py - a text-based game

class Brain:
    """A Brain handles how an NPC responds to the player character."""

    def __init__(self, response='', retortance=''):
        self.response = response
        self.retortance = retortance

    def respond(self):
        """Respond to the player's talking."""
        print(self.response)

    def retort(self):
        """Retort the player's argument."""
        print(self.retortance)

class NPC:
    """An NPC is a person or creature existing in the world."""

    def __init__(self, name, brain):
        self.name = name
        self.brain = brain

    def respond(self):
        """Respond to the player's talking."""
        self.brain.respond()

    def retort(self):
        """Retort the player's argument."""
        self.brain.retort()

class Potion:

    def __init__(self, name, count):
        self.name = name
        self.count = count

    def use(self):
        print 'You have consumed ' + self.name
        self.count -= 1

# Set up the world.
npc = NPC("Jauld", Brain(response="What's up?", retortance="I disagree!"))
revealed = False
done = False
inventory = {
    'transformation potion': Potion(name="Transformation Potion", count=1),
}

while not done:
    # Show what is around the user if it has not yet been revealed.
    if not revealed:
        print('You see ' + npc.name + ' here.')
        revealed = True

    # Get the user's command as a lowercase string.
    cmd = raw_input('> ').lower()

    # Perform the command.
    if cmd == 'talk':
        # Talk to an NPC in the current zone.
        npc.respond()
    elif cmd == 'argue':
        # Argue with an NPC in the current zone.
        npc.retort()
    elif cmd == 'look' or cmd == 'l':
        # Make the current zone show itself again.
        revealed = False
    elif cmd == 'quit' or cmd == 'q':
        # Quit the game.
        done = True
    elif cmd == 'inventory' or cmd == 'i':
        # List the contents of the player's inventory.
        for item in inventory:
            amount = inventory[item].count

            print(str(amount) + ' of ' + item)
    else:
        itemused = False

        # If the user types "use <item name>", use that item.
        for item in inventory:
            if cmd == 'use ' + item:
                inventory[item].use()
                itemused = True
                break

        # If the user did not use an item, the command is unknown.
        if not itemused:
            print('Huh?')
