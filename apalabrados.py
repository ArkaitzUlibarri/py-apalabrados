import pygame
import datetime
import os
from tile import Tile
import yaml

with open("config/config.yml", 'r') as ymlfile:
    cfg = yaml.load(ymlfile)

BONUS = cfg['bonus']
APP_NAME = cfg['appname']
FONT_SIZE = cfg['font']['size']
DEFAULT_FONT = cfg['font']['type']
FONT_BOLD = cfg['font']['bold']

USER_FICHAS = 7
SIZE = WIDTH, HEIGHT = 600, 600
MAP_SIZE = 15
SQUARE_SIZE = (WIDTH/MAP_SIZE)
MEDIUM = SQUARE_SIZE/2

Types = ["Normal","DL","DP","TL","TP","Start","Letter"]
Letters  = ["A","B","C","D","E","F","G","H","I","J","L","M","N","Ñ","O","P","Q","R","S","T","U","V","X","Y","Z","*"]
Values = [1,3,3,2,1,4,2,4,1,8,1,3,1,8,1,3,5,1,1,1,1,4,8,4,10,0]
Tiles = [12,2,4,5,12,1,2,2,6,1,4,2,5,1,9,2,1,5,6,4,5,1,1,1,1,2]

Quantity = len(Letters)
totalTiles = sum(Tiles)

letters = {'A': [1,12], 'B': [3,2], 'C': [3,4], 'D': [2,5], 'E': [1,12], 'F': [4,1], 'G': [2,2], 'H': [4,2], 'I': [1,6], 'J': [8,1], 'L': [1,4], 'M': [3,2], 
'N': [1,5], 'Ñ': [8,1], 'O':[1,9], 'P': [3,2], 'Q': [5,1], 'R': [1,5], 'S': [1,6], 'T': [1,4], 'U': [1,5], 'V': [4,1], 'X': [8,1], 'Y': [4,1], 'Z': [10,1], 
'*': [0,2] } 

class myRect(pygame.Rect):
	""" Add type property """
	def __init__(self, left, top, width, height, type):
		pygame.Rect.__init__(self, left, top, width, height)
		self.type = type

def multiplyLetter(squareType,letterValue):
	if(squareType == "DL"):
		return 2 * letterValue
	elif(squareType == "TL"):
		return 3 * letterValue
	else:
		return letterValue

def multiplyWord(squareType,wordValue):
	if(squareType == "DP"):
		return 2 * wordValue
	elif(squareType == "TP"):
		return 3 * wordValue
	else:
		return wordValue

def aplicarBonus(wordValue):
	return wordValue + BONUS

def mapeoType(number):
	return Types[number]

def loadMap(filename = "assets/map"):
	if (not os.path.isfile(filename)):
		return False

	f = open(filename, "r")
	data = f.read().split("\n")

	matrix = []
	for index,row in enumerate(data):
		matrix.append([row])

	return matrix

def main():
	pygame.init()

	font = pygame.font.SysFont(DEFAULT_FONT, FONT_SIZE, FONT_BOLD)

	screen = pygame.display.set_mode(SIZE)  # crear el canvas dónde vamos a dibujar los diferentes objetos del videojuego
	pygame.display.set_caption(APP_NAME)  # cambiar el título de la ventana

	mapr = loadMap()
	
	squares = []
	for rowIndex,rowValue in enumerate(mapr):
		rowValue = rowValue[0].split(',')
		for colIndex,colValue in enumerate(rowValue):
			#print('(' + str(rowIndex) + ',' + str(colIndex) + ') :' + str(colValue) )
			squareType = mapeoType(int(colValue))
			point = (MEDIUM + int(rowIndex) * SQUARE_SIZE,MEDIUM + int(colIndex) * SQUARE_SIZE)
			newTile = Tile(squareType,font,point)
			squares.append(newTile)

	sprites = pygame.sprite.Group(squares)

	while 1:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				return

		sprites.update() #actualice y dibuje en pantalla todos los sprites
		# screen.blit(background, (0, 0)) #copia los pixeles contenidos en la imagen de fondo sobre el canvas
		sprites.draw(screen)
		pygame.display.flip() #hacer un cambio de buffers

# Llamamos al main cuando se invoca el archivo como un programa
if __name__ == '__main__':
	print ("Game Start: "+ datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
	main()