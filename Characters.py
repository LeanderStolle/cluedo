import pygame

class Character:
    def __init__(self, name, description, color):
        self.name = name
        self.description = description
        self.color = color

fraeulein_Gloria = Character("Fräulein Gloria", "Eine junge, lebendige Frau.", Colors.rot)
oberst_senf = Character("Oberst Senf", "Ein Militärmann mit starker Persönlichkeit.", "Gelb")
herr_gruen = Character("Herr Grün", "Ein wohlhabender Geschäftsmann.", "Grün")
frau_pfau = Character("Frau Pfau", "Eine elegante und wohlhabende Frau.", "Blau")
professor_bloom = Character("Professor Bloom", "Ein intellektueller und akademischer Charakter.", "Lila")
fraeulein_weiß = Character("Fräulein Weiß", "Eine ernste und korrekte Haushälterin.", "Weiß")

