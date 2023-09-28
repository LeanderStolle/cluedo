import pygame

class Character:
    def __init__(self, game, name, description, color, x_pos, y_pos):
        self.game = game
        self.load_sprites()
        self.x_pos = x_pos
        self.y_pos = y_pos

        #Variablen Maybe for Animation
        #self.current_frame, self.last_frame_update = 0, 0

        #Character Info
        self.name = name
        self.description = description
        self.color = color


    def update(self, delta_time, actions):
        pass
        #Bewegung

        #Update Postition
        
        #Sprite Animation

    def render(self, screen):
        pass
        #Rendern des Characters auf den Screen

    def animate():
        pass
        #maybe animieren der Bewegung
        

#fraeulein_Gloria = Character("Fräulein Gloria", "Eine junge, lebendige Frau.", "Rot")
#oberst_senf = Character("Oberst Senf", "Ein Militärmann mit starker Persönlichkeit.", "Gelb")
#herr_gruen = Character("Herr Grün", "Ein wohlhabender Geschäftsmann.", "Grün")
#frau_pfau = Character("Frau Pfau", "Eine elegante und wohlhabende Frau.", "Blau")
#professor_bloom = Character("Professor Bloom", "Ein intellektueller und akademischer Charakter.", "Lila")
#fraeulein_weiß = Character("Fräulein Weiß", "Eine ernste und korrekte Haushälterin.", "Weiß")

