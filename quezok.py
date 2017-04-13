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

class DecisionBrain(Brain):
    """A DecisionBrain handles tree-based dialogues with NPCs."""

    def __init__(self, states):
        """Create a DecisionBrain with the given states.

        Dialogue always starts on the 'intro' state.

        The states dictionary should have the following form:

        {
            'intro': {
                'text': 'Jauld stammers at you.',
                'respond': 'slowly',
                'retort': 'fearful'
            },
            'slowly': {
                'text': 'Jauld gathers his senses and gives his tale.',
                'respond': None,
                'retort': None
            },
            'slowly': {
                'text': 'Jauld disappears into his cloak.',
                'respond': None,
                'retort': None
            }
        }"""
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
        print 'You have consumed ' + self.name
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
