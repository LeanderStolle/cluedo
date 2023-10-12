import player


class TurnHandler:
    def __init__(self, players):
        self.players = players
        self.current_turn = 0

    def next_turn(self):
        self.current_turn = (self.current_turn + 1) % len(self.players)

    def get_current_player(self):
        return self.players[self.current_turn]