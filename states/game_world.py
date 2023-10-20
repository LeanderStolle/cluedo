from player import *
from turn_handler import *
from button import Button
from card_stack import *
from states.dice import *
from board import *
from states.suspicion import Suspicion
from states.accusation import Accusation

class Game_World(State):
    def __init__(self, game, selected_players):
        State.__init__(self, game)

        self.actions = {"pause": False, "note":False}


        self.game_board = Board()
        self.dice = Dice()
        self.dice.roll()
        self.dice_result = self.dice.get_sum()
        # Player related shit
        self.selected_players = selected_players
        
        self.tmp_list = []
        factory = PlayerFactory()
        for elem in self.selected_players:
            self.tmp_list.append(factory.create_player(elem))

        self.active_players = self.tmp_list

        def give_cards_to_players():
            num_players = len(self.active_players)
            cards_per_player = len(combined_cardstack) // num_players
            remaining_cards = len(combined_cardstack) % num_players

            for player in self.active_players:
                num_cards_to_draw = cards_per_player
                if remaining_cards > 0:
                    num_cards_to_draw += 1
                    remaining_cards -= 1

                for _ in range(num_cards_to_draw):
                    player.add_card(combined_cardstack.draw_card())

        give_cards_to_players()

        def print_cards_of_each_player():
            for player in self.active_players:
                print("player name:" + player.name)
                for card in player.card_list:
                    print(card.name)
        print_cards_of_each_player()
        # Turnhandler
        self.turnhandler = TurnHandler(self.active_players)

        print(self.turnhandler.current_player)

        # Buttons for player interaction
        self.suspect_btn = Button(self.game, "Suspect", 25, 850, 150, 40, True)
        self.accuse_btn = Button(self.game, "Accuse", 200, 850, 150, 40, True)
        self.endturn_btn = Button(self.game, "End Turn", 25, 900, 150, 40, True)
        self.cards_btn = Button(self.game, "Show Cards", 200, 900, 150, 40, True)
        self.back_btn = Button(self.game, "Back", 300, 600, 150, 40, True)

        # Text for player interaction
        self.active_player_text = "test"
        self.popup_text = "test1"

        self.cardv = False

    def get_neighbours(self, given_tile):
        neighbours = []
        for tile in self.game_board.board:
            if tile.type == 'Wall' or tile.name == given_tile.name:
                continue  # Skip wall tiles and the given tile

            # Check if tiles are horizontally adjacent
            if (given_tile.y < tile.y + tile.height) and (tile.y < given_tile.y + given_tile.height):
                gap = 5 if (tile.type == 'Room' or given_tile.type == 'Room') else 0
                if abs((tile.x + tile.width / 2) - (given_tile.x + given_tile.width / 2)) <= (
                        tile.width + given_tile.width) / 2 + gap:
                    neighbours.append(tile)

            # Check if tiles are vertically adjacent
            if (given_tile.x < tile.x + tile.width) and (tile.x < given_tile.x + given_tile.width):
                gap = 5 if (tile.type == 'Room' or given_tile.type == 'Room') else 0
                if abs((tile.y + tile.height / 2) - (given_tile.y + given_tile.height / 2)) <= (
                        tile.height + given_tile.height) / 2 + gap:
                    neighbours.append(tile)
        return neighbours

    def find_possible_moves(self, tile, steps):
        possible_moves = set()
        current_tiles = [tile]
        for _ in range(steps):
            next_tiles = []
            for t in current_tiles:
                neighbours = self.get_neighbours(t)
                for neighbour in neighbours:
                    if neighbour.type == "Room":
                        # Stop searching if a room is reached
                        possible_moves.add(neighbour)
                    elif neighbour not in possible_moves and neighbour.type != "Wall":
                        possible_moves.add(neighbour)
                        next_tiles.append(neighbour)
            current_tiles = next_tiles
        return list(possible_moves)

    def draw_possible_moves(self,steps,screen):
        possible_moves = self.find_possible_moves(self.game_board.find_tile_by_name(self.turnhandler.current_player.tile), steps)
        border_color = (255,160,122)
        border_size = 1
        playerpos = []
        for player in self.active_players:
            playerpos.append(self.game_board.find_tile_by_name(player.tile))
        for tile in possible_moves:
            print(tile)
            if tile in playerpos and tile.type == "Room":
                continue
            if tile.type == "Wall":
                continue
            pygame.draw.rect(screen, border_color, (tile.x, tile.y, tile.width, border_size))
            # Draw bottom border
            pygame.draw.rect(screen, border_color,(tile.x, tile.y + tile.height - border_size, tile.width, border_size))
            # Draw left border
            pygame.draw.rect(screen, border_color, (tile.x, tile.y, border_size, tile.height))
            # Draw right border
            pygame.draw.rect(screen, border_color,(tile.x + tile.width - border_size, tile.y, border_size, tile.height))


    def update(self, delta_time, actions):
        if self.cards_btn.clicked:
            self.cardv = True
            self.cards_btn.clicked = False
        if self.back_btn.clicked:
            self.cardv = False
            self.back_btn.clicked = False
        if self.suspect_btn.clicked:
            new_state = Suspicion(self.game,self.active_players,self.turnhandler.current_player)
            new_state.enter_state()
            self.suspect_btn.clicked = False
        if self.accuse_btn.clicked:
            new_state = Accusation(self.game,self.active_players,self.turnhandler.current_player)
            new_state.enter_state()
            self.accuse_btn.clicked = False
        if self.endturn_btn.clicked:
            self.dice.roll()
            self.dice_result = self.dice.get_sum()
            self.turnhandler.current_player.move = True
            self.turnhandler.current_player.suspect = True
            self.turnhandler.end_turn() # Endturn logic
            self.endturn_btn.clicked = False
        self.game.reset_keys()

    def render(self, screen):
        screen.fill((255,255,255))
        self.game_board.draw_board(screen)
        self.draw_players(screen)
        self.draw_player_hand(self.turnhandler.current_player, (0, 0), screen)
        self.cards_btn.draw()
        self.suspect_btn.draw()
        self.accuse_btn.draw()
        self.endturn_btn.draw()
        self.game.draw_text(screen, ("Its " +str(self.turnhandler.current_player.name) + "´s turn!") , "black", 200, 775)
        self.game.draw_text(screen, ("You rolled a " + str(self.dice_result)) , "black", 200, 825)
        self.draw_player_hand(self.turnhandler.current_player, (0, 0), screen)
        self.draw_possible_moves(self.dice_result, screen)
        self.draw_players(screen)
        pygame.display.flip()  # Update the display
        

    def handle_click(self, x, y, board):
            for tile in board:
                if tile.contains_point(x, y):
                    print("Dieses Tile habe ich geklicked", tile.name)
                    return tile
                if tile.contains_point(x, y) and tile.type == "wall":
                    print("Hier kann man nicht hinlaufen", tile.name)
                    return tile
            return None

    def draw_player_hand(self,player, start_position,screen):
        if self.cardv:
            screen.fill((255,255,255))
            self.back_btn.draw()
            x, y = start_position
            for card in player.card_list:
                card.draw_card(card, (x, y),screen)
                x += 160  # Adjust this spacing based on your preferenc
                if x > 450:
                    y += 200
                    x = 0



    def draw_players(self, screen):
        for player in self.active_players:
            tile_center = self.game_board.find_tile_by_name(player.tile).get_center()
            if player == self.turnhandler.current_player:
                pygame.draw.circle(screen, (255, 255, 255), tile_center, 10)
                pygame.draw.circle(screen, player.rgb,tile_center,6)
            else:
                pygame.draw.circle(screen, player.rgb, tile_center, 6)

    def player_move(self, given_tile):
        playerpos = []
        for player in self.active_players:
            if self.game_board.find_tile_by_name(player.tile) == given_tile and given_tile.type != "Room":
                return
            playerpos.append(self.game_board.find_tile_by_name(player.tile))
        if given_tile in self.find_possible_moves(self.game_board.find_tile_by_name(self.turnhandler.current_player.tile), self.dice_result) and self.turnhandler.current_player.move:
            self.turnhandler.current_player.tile = given_tile.name
            self.turnhandler.current_player.move = False



    def get_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit(0)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.actions["pause"] = True  
                if event.key == pygame.K_SPACE:
                    self.actions["note"] = True   
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos  # Get the x, y position of the click
                if self.game_board.find_tile_at_position(x,y) in self.game_board.board and self.cardv == False:
                    self.player_move(self.game_board.find_tile_at_position(x,y))
                if self.cards_btn.check_click(x,y):
                    self.cards_btn.clicked = not self.cards_btn.clicked
                if self.suspect_btn.check_click(x,y):
                    if self.game_board.find_tile_by_name(self.turnhandler.current_player.tile).type != "Room" or self.turnhandler.current_player.suspect == False:
                        print("You are not in a room")
                    elif self.game_board.find_tile_by_name(self.turnhandler.current_player.tile).type == "Room":
                        self.suspect_btn.clicked = not self.suspect_btn.clicked
                if self.accuse_btn.check_click(x,y):
                    self.accuse_btn.clicked = not self.accuse_btn.clicked
                if self.endturn_btn.check_click(x,y):
                    self.endturn_btn.clicked = not self.endturn_btn.clicked
                if self.back_btn.check_click(x,y):
                    self.back_btn.clicked = not self.back_btn.clicked



#TO-DO:
#  2. Waffen platzieren
#  4. übrige Karten auf Stapel aufteilen ( Personen, Waffen, Räume), dann mischen und auch verdeckt platzieren --> Jan
#  5. von jedem Stapel (Personen, Waffe, Räume) muss eine Karte in die Fallakte (Lösung) --> Jan
#  6. Mischen der übrigen Karten und verteilen an Spieler (nicht schlimm wenn jemand mehr Karten hat als der andere) --> Jan
#  7. Spielstart --> möglichkeit seine Karten anzuschauen (im eigenen Spielzug)
#     roll dice --> passiert am anfang des zuges von jedem Player


# Notwendige Buttons: --> Leander
# - show cards (bilder?)
# - end turn --> prio
# - note???
# - suspect button
# - accuse button
#  
# Allgemeines:
# - maybe UI mit aktivem Spielernamen, Buttons fürs Würfel, anschuldigen, karten anschauen, notes taken
#
# actions für jeden State definieren und in game.py bei update die actions für jeden State mitgeben

#macht keinen sinn board in gameworld klasse zu speichern da man immer ein objekt erstellen muss um es zu referenzieren