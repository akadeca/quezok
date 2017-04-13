#! /usr/bin/env python
# quezok.py - a text-based game

done = False
while not done:
    # Get the user's command as a lowercase string.
    cmd = raw_input('> ').lower()

    # Perform the command.
    if cmd == 'quit' or cmd == 'q':
        done = True
