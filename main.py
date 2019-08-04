#*-* coding: utf-8 *-*

import pygame, sys
import pygame.locals as GAME_GLOBALS
import pygame.event as GAME_EVENTS
#from Torre import *

pygame.init()
Reloj = pygame.time.Clock()

#Variables Globales
windowsWidth = 1000
windowsHeight = 700
GameStarted = True
GameEnding = False

Surface = pygame.display.set_mode((windowsWidth, windowsHeight))
pygame.display.set_caption('Ajedrez 2.0')

#Colores de uso de todos 
ColorNegro = (0, 0, 0)
ColorBlanco = (255, 255, 255)

#Variables referentes al raton
MousePosition = None
MousePressed = False
Punteador = False

#Posicion en el tablero del juego
CuadradoXY = 75		#CuadradoY = 100
PosicionTabX = 200
PosicionTabY = 50
RelojTablero = False	#Empieza de color negro

#MARCO PARA EL TABLERO DE AJEDREZ
MarcoTab = pygame.image.load("Recursos/img/MarcoTab.png")

def MarcoTablero():
	global MarcoTab, PosicionTabX, PosicionTabY

	MarcoBorder = MarcoTab.get_rect()
	MarcoBorder.centerx = 500
	MarcoBorder.centery = 350

	Surface.blit(MarcoTab, MarcoBorder)

def Tablero():
	global CuadradoXY, ColorNegro, ColorBlanco, RelojTablero
	PosicionTabX1 = 200
	PosicionTabY1 = 50
	cont = 0

	for i in range(8):
		PosicionTabX1 = 200
		if RelojTablero == False:
			ColorTab = ColorNegro
			RelojTablero = True
		else:
			ColorTab = ColorBlanco
			RelojTablero = False

		if PosicionTabY1 >= 600 or PosicionTabY1 >= 600 - CuadradoXY:
				PosicionTabY1 = windowsHeight - CuadradoXY - 50

		if cont >= 1:
			PosicionTabY1 += 75

		pygame.draw.rect(Surface, ColorTab, (PosicionTabX1, PosicionTabY1, CuadradoXY, CuadradoXY))
		cont += 1

		for j in range(8):
			PosicionTabX1 += 75

			if RelojTablero == False:
				ColorTab = ColorNegro
				RelojTablero = True
			else:
				ColorTab = ColorBlanco
				RelojTablero = False

			if PosicionTabY1 >= 650 or PosicionTabY1 >= 600 - CuadradoXY:
				#print(PosicionTabY1, PosicionTabX2, PosicionTabX1)
				PosicionTabY1 = windowsHeight - CuadradoXY - 50

			if PosicionTabX1 >= 800:
				PosicionTabX1 = 725 - CuadradoXY

			pygame.draw.rect(Surface, ColorTab, (PosicionTabX1, PosicionTabY1, CuadradoXY, CuadradoXY))

class TorreFicha():

	#
	def __init__(self, windowsHeight, CuadradoXY, PosicionTabX, PosicionTabY):
		#Variables para la Ficha Torre Blanca y Negra
		self.Height = windowsHeight
		self.Cuadrado = CuadradoXY
		self.Posicionx = PosicionTabX
		self.Posiciony = PosicionTabY
		self.DetectorFicha = False
		
		self.Torre1 = pygame.image.load("Recursos/img/TorreBlanca1.png")	#Torre Blanca
		self.Torre2 = pygame.image.load("Recursos/img/TorreNegra1.png")	#Torre Negra

		#Posicionamiento de Torre Blanca INICIAL
		self.rectTorre = self.Torre1.get_rect()
		self.rectTorre.centerx = self.Posicionx + 36
		self.rectTorre.centery = self.Posiciony + 36

		#Posicionamiento de Torre Negra INICIAL
		self.rectTorre1 = self.Torre2.get_rect()
		self.rectTorre1.centerx = self.Posicionx + 36 + (75*7)
		self.rectTorre1.centery = (self.Posiciony + 36)

	def MoveTorre(self, MousePosition, MousePressed, Punteo, Surface):		#EL ERROR ESTA EN TODO ESTE METODO MOVETORRE
		if MousePressed == True:
			#Comprobamos que el raton esta colocado sobre el cuadro que hemos definido
			if MousePosition[0] > self.rectTorre.centerx - 36 or MousePosition[0] < self.rectTorre.centerx - 36 + self.Cuadrado:
				if MousePosition[1] > self.rectTorre.centery - 36 or MousePosition[1] < self.rectTorre.centery - 36 + self.Cuadrado:
					pygame.draw.rect(Surface, (139, 142, 44, 0.1), (self.rectTorre.centerx - 36, self.rectTorre.centery - 36, self.Cuadrado, self.Cuadrado))
					Punteo = True
					print(" lol",Punteo, "y:", self.rectTorre.centery)
					pygame.mouse.set_visible(1)
					self.DetectorFicha = True
		else:
			#SquareColor = (255, 0, 0)
			pygame.mouse.set_visible(1)
			Punteo = False

		if Punteo == True:
			self.colorSelector = (139, 142, 44, 0.1)
			self.rectTorre.centerx = MousePosition[0] #- self.rectTorre.centerx + 200
			self.rectTorre.centery = MousePosition[1] #- self.rectTorre.centery + 200
			if self.rectTorre.centerx > self.Posicionx:
				if self.rectTorre.centerx >= self.Posicionx + (75*7) and MousePressed == False:
					self.rectTorre.centerx = self.Posicionx + 36 + (75*7)
				elif self.rectTorre.centerx < self.Posicionx + (75*7) and MousePressed == False:
					self.rectTorre.centerx = MousePosition[0]
				else:
					self.rectTorre.centerx = MousePosition[0]
				
				if self.rectTorre.centery > self.Posiciony and MousePressed == False:

					if self.rectTorre.centery >= self.Posiciony + (75*7) and MousePressed == False:
						self.rectTorre.centery = self.Posiciony + 36 + (75*7)
					elif self.rectTorre.centery < self.Posiciony + (75*7) and MousePressed == False:
						self.rectTorre.centery = MousePosition[1]
					else:
						self.rectTorre.centery = MousePosition[1]
			
			Surface.blit(self.Torre1, self.rectTorre)

	def dibujarTorres(self, superficie):
		superficie.blit(self.Torre1, self.rectTorre)
		superficie.blit(self.Torre2, self.rectTorre1)

def QuitGame():

	pygame.quit()
	sys.exit()

while True:
	#Variables del juego
	#InGame = True								/// DAR UN USO A ESTA VARIABLE PARA CONTROLAR EL INICIO DEL JUEGO
	MousePosition = pygame.mouse.get_pos()

	Surface.fill((190, 190, 190))

	#Comprobamos sí estamos punsando el ratón
	if pygame.mouse.get_pressed()[0]  == True:
		MousePressed = True
	else:
		MousePressed = False

	#Fondo de pantalla del juego
	FondoPantalla = pygame.image.load("Recursos/img/FondoPantalla.jpg")
	torre = TorreFicha(windowsHeight, CuadradoXY, PosicionTabX, PosicionTabY)
	#Comprobamos sí estamos punsando el ratón
	'''
	if pygame.mouse.get_pressed()[0]  == True:
		MousePressed = True
	else:
		MousePressed = False
	'''
	Reloj.tick(60)

	for event in GAME_EVENTS.get():

		'''
		if InGame == True:
			if event.type == :
				pass
		'''
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE:
				QuitGame()

		if event.type == pygame.KEYUP:
			pass

		if event.type == GAME_GLOBALS.QUIT:
			QuitGame()
	
	Surface.blit(FondoPantalla, (0, 0))
	MarcoTablero()
	Tablero()
	torre.dibujarTorres(Surface)
	torre.MoveTorre(MousePosition, MousePressed, Punteador, Surface)
	Reloj.tick(60)
	pygame.display.update()