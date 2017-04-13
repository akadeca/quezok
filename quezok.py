#! /usr/bin/env python
# quezok.py - a text-based game

class DecisionBrain:
    """A DecisionBrain handles tree-based dialogues with NPCs."""

    def __init__(self, states):
        """Create a DecisionBrain with the given states dictionary.

        The states dictionary should have state names as keys
        and states themselves as values.

        A state in itself is a dictionary with the keys 'text',
        'respond', and 'retort' which are, respectively, the message
        text to be printed when the state is reached, the name of
        the state to change to if the user talks, and the state to
        change to if the user argues.  If 'respond' is None, talking
        will not change the state.  If 'retort' is None, arguing will
        not change the state.

        Dialogue always starts on the 'intro' state.
        """
        self.states = states
        self.state = {'text': '', 'respond': 'intro', 'retort': 'intro'}

    def respond(self):
        """Respond to the player's talking."""
        if self.state is None or self.state['respond'] is None:
            print('No one is willing to talk.')
            return

        self.state = self.states[self.state['respond']]

        if self.state is not None:
            print(self.state['text'])

    def retort(self):
        """Retort the player's argument."""
        if self.state is None or self.state['retort'] is None:
            print('No one is willing to argue.')
            return

        self.state = self.states[self.state['retort']]

        if self.state is not None:
            print(self.state['text'])

class NPC:
    """An NPC is a person or creature existing in the world."""

    def __init__(self, name, brain):
        """Create a new NPC with the given name and brain.

        The brain can be any object, but it must have two methods:
        .respond() and .retort().
        """
        self.name = name
        self.brain = brain

    def respond(self):
        """Respond to the player's talking."""
        self.brain.respond()

    def retort(self):
        """Retort the player's argument."""
        self.brain.retort()

class Potion:
    """A Potion is an item which can be consumed."""

    def __init__(self, name, count):
        self.name = name
        self.count = count

    def use(self):
        if self.count <= 0:
            print("You don't have any more of those.")
        else:
            print('You have consumed ' + self.name)
            self.count -= 1

# Set up our NPC.
npc = NPC('Stin', DecisionBrain({
    'intro': {
        'text': "Stin tries to explain himself.  It wasn't his fault!",
        'respond': 'glad',
        'retort': 'sad'
    },
    'glad': {
        'text': "Stin is happy that you don't blame him.",
        'respond': None,
        'retort': None
    },
    'sad': {
        'text': "Stin runs away with crocodile tears in his eyes.",
        'respond': None,
        'retort': None,
    }
}))

# Set up the world.
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
