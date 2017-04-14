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
