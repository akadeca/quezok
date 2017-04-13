#! /usr/bin/env python
# quezok.py - a text-based game

class Brain:
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
    def __init__(self, name, brain):
        self.name = name
        self.brain = brain

    def respond(self):
        """Respond to the player's talking."""
        self.brain.respond()

    def retort(self):
        """Retort the player's argument."""
        self.brain.retort()

npc = NPC("Jauld", Brain(response="What's up?", retortance="I disagree!"))
done = False
while not done:
    # Get the user's command as a lowercase string.
    print('You see ' + npc.name + ' here.')
    cmd = raw_input('> ').lower()

    # Perform the command.
    if cmd == 'talk':
        # Talk to an NPC in the current zone.
        npc.respond()
    elif cmd == 'argue':
        # Argue with an NPC in the current zone.
        npc.retort()
    elif cmd == 'quit' or cmd == 'q':
        # Quit the game.
        done = True
