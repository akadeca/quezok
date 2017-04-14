class Player:
    """A Player represents the player character."""

    def __init__(self):
        """Create a new player character."""
        self.transformed = False

    def transform(self):
        """Attempt to transform the player character."""
        if self.transformed:
            print('Nothing happens.')
        else:
            print('You become a hideous monstrosity.')
            self.transformed = True

    def untransform(self):
        """Attempt to untransform (humanize) the player character."""
        if self.transformed:
            print('You become regular old you.')
            self.transformed = False
        else:
            print('Nothing happens.')
