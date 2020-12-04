#Importation des bibliothèques nécessaires
import pygame
from pygame.locals import *
from classes import *



#Initialisation de la bibliothèque Pygame
pygame.init()

#Création de la fenêtre
fenetre = pygame.display.set_mode((450,450))


#Image de fond
fond = pygame.image.load("fond_vert.png").convert()
fenetre.blit(fond, (0,0))
niveau = Niveau('n1')
niveau.generer()
niveau.afficher(fenetre)

#personnage
perso = Perso("perso3.png", "perso4.png",
		"perso2.png", "perso1.png", niveau)

persos =Perso("mario1.png", "mario2.png",
	 "mario3.png", "mario4.png", niveau)

persos.x=390
persos.y=390

perso.x=30
perso.y=30




pygame.display.flip() #rafraichir la page
bombes = []
t = pygame.time.get_ticks()


#Variable qui continue la boucle si = 1, stoppe si = 0
continuer = 1

pygame.key.set_repeat(400, 30) #si on reste appuyé sur la touche le perso se deplace tant qu'on reste appuyé

#Boucle infinie
while continuer:
	for event in pygame.event.get():   #On parcours la liste de tous les événements reçus
		if event.type == QUIT:     #Si un de ces événements est de type QUIT
			continuer = 0      #On arrête la boucle

		if event.type == KEYDOWN:
			if event.key == K_DOWN:
					perso.deplacer('bas')

			if event.key == K_UP:
				perso.deplacer('haut')

			if event.key == K_LEFT:
				perso.deplacer('gauche')

			if event.key == K_RIGHT:
				perso.deplacer('droite')

			if event.key == K_e:
				persos.deplacer('haut')

			if event.key == K_f:
				persos.deplacer('droite')

			if event.key == K_d:
				persos.deplacer('bas')

			if event.key == K_s:
				persos.deplacer('gauche')

			if event.key == K_SPACE:
					print("bombe")#a remplacer par la pose de la bombe.
					bombes.append(Bombe("bombe.png", niveau, (perso.x, perso.y), pygame.time.get_ticks()))

			if event.key == K_r:
					print("bombe")#a remplacer par la pose de la bombe.
					bombes.append(Bombe("bombe.png", niveau, (persos.x, persos.y), pygame.time.get_ticks()))

#remet le fond et le perso
	fenetre.blit(fond, (0,0))
	niveau.afficher(fenetre)
	fenetre.blit(perso.direction, (perso.x, perso.y))
	fenetre.blit(persos.direction, (persos.x, persos.y))
	for i in range(len(bombes)):
		bombes[i].update(pygame.time.get_ticks())
		if bombes[i].explose:
			del bombes[i]
			pass

	for i in range(len(bombes)):
		bombes[i].afficher(fenetre)
	pygame.display.flip()

pygame.display.quit();

