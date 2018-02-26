import pygame

class Ficha(pygame.sprite.Sprite):
	SIZE = (40,40) # 40x40

	dic_colores = {'amarillo': (255,239,25), 'blanco': (255,255,255), 'rojo': (255,0,0), 'verde': (0,255,0), 
	'azul': (0,0,255), 'naranja': (239,127,26), 'morado': (163,73,164)}

	def __init__(self,tipo,font,pos=(0,0)):
		pygame.sprite.Sprite.__init__(self)
		self.pos = pos
		self.tipo = tipo
		self.text = self.setText()
		self.color = self.setColor()

		self.image = pygame.Surface(Ficha.SIZE).convert()
		self.image.fill(self.color)
		self.rect = self.image.get_rect(center=self.pos)

		self.font = font
		#self.image = self.font.render(str(self.text), 0, self.dic_colores['blanco'], self.color)
		self.image = self.font.render(str(self.text), 0, self.dic_colores['blanco'])
		#self.rect = self.image.get_rect(center=self.pos)

		#self.valor = 0
		#self.cantidad = 0

	def show(self):
		print(self.pos)

	def setColor(self):
		if(self.tipo == "Normal"):
			return self.dic_colores['blanco']
		elif(self.tipo == "DL"):
			return self.dic_colores['azul'] 
		elif(self.tipo == "DP"):
			return self.dic_colores['naranja']  
		elif(self.tipo == "TL"):
			return self.dic_colores['verde']  
		elif(self.tipo == "TP"):
			 return self.dic_colores['rojo']  
		elif(self.tipo == "Inicio"):
			return self.dic_colores['morado']   
		elif(self.tipo == "Letra"):
			return self.dic_colores['amarillo']

	def setText(self):
		if(self.tipo == "Normal" or self.tipo == "Inicio" or self.tipo == "Letra"):
			return ""
		else:
			return self.tipo