import player



class TurnHandler:
    def __init__(self, player_order: list):
        self.player_order = player_order
        self.current_player_index  = 0
        self.current_player = self.player_order[self.current_player_index]



    def next_turn(self):

        self.current_player_index = (self.current_player_index + 1) % len(self.player_order)
        self.current_player = self.player_order[self.current_player_index]
        while not self.current_player.playing:
            # If player is not playing, skip to the next player
            self.current_player_index = (self.current_player_index + 1) % len(self.player_order)
            self.current_player = self.player_order[self.current_player_index]

    def is_player_turn(self, player_color):
        return player_color == self.current_player

    def end_turn(self):
        self.next_turn()

