
import pygame
from pygame.locals import *


nombre_sprite_cote = 15
taille_sprite = 30
cote_fenetre = nombre_sprite_cote * taille_sprite


class Niveau:
	"""Classe permettant de créer un niveau"""
	def __init__(self, fichier):
		self.fichier = fichier
		self.structure = 0


	def generer(self):
		"""Méthode permettant de générer le niveau en fonction du fichier.
		On crée une liste générale, contenant une liste par ligne à afficher"""
		#On ouvre le fichier
		with open(self.fichier, "r") as fichier:
			structure_niveau = []
			#On parcourt les lignes du fichier
			for ligne in fichier:
				ligne_niveau = []
				#On parcourt les sprites (lettres) contenus dans le fichier
				for sprite in ligne:
					#On ignore les "\n" de fin de ligne
					if sprite != '\n':
						#On ajoute le sprite à la liste de la ligne
						ligne_niveau.append(sprite)
				#On ajoute la ligne à la liste du niveau
				structure_niveau.append(ligne_niveau)
			#On sauvegarde cette structure
			self.structure = structure_niveau


	def afficher(self, fenetre):
		"""Méthode permettant d'afficher le niveau en fonction
		de la liste de structure renvoyée par generer()"""
		#Chargement des images
		mur = pygame.image.load("incassable.png").convert()
		destructible = pygame.image.load("mur.png").convert()

		#On parcourt la liste du niveau
		num_ligne = 0
		for ligne in self.structure:
			#On parcourt les listes de lignes
			num_case = 0
			for sprite in ligne:
				#On calcule la position réelle en pixels
				x = num_case * taille_sprite
				y = num_ligne * taille_sprite
				if sprite == 'm':		   #m = Mur
					fenetre.blit(mur, (x,y))
				elif sprite == 'd':		   #d = Déstructible
					fenetre.blit(destructible, (x,y))

				num_case += 1
			num_ligne += 1




class Perso:
	"""Classe permettant de créer un personnage"""
	def __init__(self, droite, gauche, haut, bas, niveau):

        #Sprites du personnage
		self.droite = pygame.image.load(droite).convert()
		self.droite.set_colorkey((255, 255, 255))

		self.gauche = pygame.image.load(gauche).convert()
		self.gauche.set_colorkey((255, 255, 255))

		self.haut = pygame.image.load(haut).convert()
		self.haut.set_colorkey((255, 255, 255))

		self.bas = pygame.image.load(bas).convert()
		self.bas.set_colorkey((255, 255, 255))

        #Position du personnage en cases et en pixels
		self.case_x = 0
		self.case_y = 0
		self.x = 0
		self.y = 0

        #Direction par défaut
		self.direction = self.droite

        #Niveau dans lequel le personnage se trouve
		self.niveau = niveau

	def deplacer(self, direction):
		"""Methode permettant de déplacer le personnage"""

		#Déplacement vers la droite
		if direction == 'droite':
            #Pour ne pas dépasser l'écran
			if self.case_x < (nombre_sprite_cote - 1):
                #On vérifie que la case de destination n'est pas un mur
				if self.niveau.structure[self.case_y][self.case_x+1] != 'm'and self.niveau.structure[self.case_y][self.case_x+1] != 'd':
					#Déplacement d'une case
					self.case_x += 1
					#Calcul de la position "réelle" en pixel
					self.x = self.case_x * taille_sprite
			#Image dans la bonne direction
			self.direction = self.droite

		#Déplacement vers la gauche
		if direction == 'gauche':
			if self.case_x > 0:
				if self.niveau.structure[self.case_y][self.case_x-1] != 'm'and self.niveau.structure[self.case_y][self.case_x-1] != 'd':
					self.case_x -= 1
					self.x = self.case_x * taille_sprite
			self.direction = self.gauche

		#Déplacement vers le haut
		if direction == 'haut':
			if self.case_y > 0:
				if self.niveau.structure[self.case_y-1][self.case_x] != 'm'and self.niveau.structure[self.case_y-1][self.case_x] != 'd':
					self.case_y -= 1
					self.y = self.case_y * taille_sprite
			self.direction = self.haut

		#Déplacement vers le bas
		if direction == 'bas':
			if self.case_y < (nombre_sprite_cote - 1):
				if self.niveau.structure[self.case_y+1][self.case_x] != 'm'and self.niveau.structure[self.case_y+1][self.case_x] != 'd':
					self.case_y += 1
					self.y = self.case_y * taille_sprite
			self.direction = self.bas


class Bombe:
    """Classe permettant de créer la bombe"""
    def __init__(self, forme, niveau, position, t):
        #Sprites de la bombe
        self.forme = pygame.image.load("bombe.png").convert()
        self.forme.set_colorkey((255, 255, 255))
        self.niveau = niveau
        self.pos = position
        self.t = t
        self.explose = False

    def update(self, t):
        if t - self.t > 1000:
            self.explose = True

            if (int(self.pos[0]//taille_sprite)) > 0:

                if self.niveau.structure[int(self.pos[1]//taille_sprite)][int((self.pos[0]//taille_sprite) - 1)] == "d":
                    self.niveau.structure[int(self.pos[1]//taille_sprite)][int((self.pos[0]//taille_sprite) - 1)] = 0

                if self.niveau.structure[int(self.pos[1]//taille_sprite)][int((self.pos[0]//taille_sprite) + 1)] == "d":
                    self.niveau.structure[int(self.pos[1]//taille_sprite)][int((self.pos[0]//taille_sprite) + 1)] = 0



            if (int(self.pos[1]//taille_sprite)) < nombre_sprite_cote:


                if self.niveau.structure[int((self.pos[1]//taille_sprite) - 1)][int(self.pos[0]//taille_sprite)] == "d":
                    self.niveau.structure[int((self.pos[1]//taille_sprite) - 1)][int(self.pos[0]//taille_sprite)] = 0

                if self.niveau.structure[int((self.pos[1]//taille_sprite) + 1)][int(self.pos[0]//taille_sprite)] == "d":
                    self.niveau.structure[int((self.pos[1]//taille_sprite) + 1)][int(self.pos[0]//taille_sprite)] = 0



    def afficher(self, fenetre):
        fenetre.blit(self.forme, self.pos)
