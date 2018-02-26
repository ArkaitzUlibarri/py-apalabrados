import pygame
#from ficha import Ficha

class Letra(Ficha):
	size = (50,50)#1x1
	color = (255,239,25)#Amarillo

	def __init__(self,tipo,pos=(0,0)):
		pygame.sprite.Sprite.__init__(self)
		self.pos = pos
		self.image = pygame.Surface(Ficha.size).convert()
		self.image.fill(self.color)
		self.tipo = tipo
		#self.valor = 0
		#self.cantidad = 0

	def show():
		print(self.tipo)