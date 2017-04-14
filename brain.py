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
