class NoPlayersError(Exception):
    def __init__(self):
        super().__init__()


class PlayersListError(Exception):
    def __init__(self):
        super().__init__()


class AddPlayerError(Exception):
    def __init__(self):
        super().__init__()


class DeletePlayerError(Exception):
    def __init__(self):
        super().__init__()
