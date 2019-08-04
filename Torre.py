#*-* coding: utf-8 *-*

import pygame, sys
import pygame.locals as GAME_GLOBALS
import pygame.event as GAME_EVENTS
from main import *

#Variables a usar

class TorreFicha(windowsWidth, windowsHeight, CuadradoXY, PosicionTabX):
	#
	def __init__(self):
		self.Torre1 = pygame.image.load("Recursos/img/torreBlanca.png")

		self.rect = self.Torre1.get_rect()
		self.rect.centerx = PosicionTabX
		self.rect.centery = windowsHeight - CuadradoXY - PosicionTabY

	def dibujar(self, superficie):
		superficie.blit(self.Torre1, self.rect)
