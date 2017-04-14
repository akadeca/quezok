#! /usr/bin/env python
# quezok.py - a text-based game
from brain import DecisionBrain
from npc import NPC
from item import Item

# Set up our NPCs.
stin = NPC('Stin', DecisionBrain({
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

jauld = NPC('Jauld', DecisionBrain({
    'intro': {
        'text': "Jauld waves.",
        'respond': 'intro',
        'retort': 'bicker'
    },
    'bicker': {
        'text': "Jauld furrows his eyebrows at you.",
        'respond': 'intro',
        'retort': 'bicker'
    }
}))

# Set up the world.
revealed = False
done = False
transformed = False

def transform():
    """Transform the player into a monster."""
    global transformed

    if transformed:
        print('Nothing happens.')
    else:
        print('You become something monstrous.')
        transformed = True

def untransform():
    """Transform the player into a human."""
    global transformed

    if transformed:
        print('You become your old self.')
        transformed = False
    else:
        print('Nothing happens.')

inventory = {
    'dusty flute':
      Item(name="Dusty Flute", count=1, verb='play', act=transform),
    'origin relic':
      Item(name="Origin Relic", count=1, verb='honor', act=untransform)
}

zone = {'description': 'The pier is long and unforgiving.',
        'npc': stin}
otherzone = {'description': 'Under this lighthouse the stars are gone.',
             'npc': jauld}

while not done:
    # Show what is around the user if it has not yet been revealed.
    if not revealed:
        print(zone['description'])
        print('You see ' + zone['npc'].name + ' here.')
        revealed = True

    # Get the user's command as a lowercase string.
    cmd = raw_input('> ').lower()

    # Perform the command.
    if cmd == 'talk':
        # Talk to an NPC in the current zone.
        zone['npc'].respond()
    elif cmd == 'argue':
        # Argue with an NPC in the current zone.
        zone['npc'].retort()
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
    elif cmd == 'go' or cmd == 'g':
        # Switch zones.
        tmp = zone
        zone = otherzone
        otherzone = tmp
        revealed = False
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
