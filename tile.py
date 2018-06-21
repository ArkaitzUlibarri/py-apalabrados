import pygame

class Tile(pygame.sprite.Sprite):
	SIZE = (WIDTH, HEIGHT) = (40,40) # 40x40

	dic_colors = {'yellow': (255,239,25), 'white': (255,255,255), 'red': (255,0,0), 'green': (0,255,0), 
	'blue': (0,0,255), 'orange': (239,127,26), 'black': (0,0,0)}

	def __init__(self,squareType,font,pos=(0,0)):
		pygame.sprite.Sprite.__init__(self)
		self.pos = pos
		self.squareType = squareType
		self.text = self.setText()
		self.color = self.setColor()
		self.font = font
		self.image = pygame.Surface(Tile.SIZE).convert()
		self.image.fill(self.color)
		label = self.font.render(str(self.text), 0, self.dic_colors['white'])
		coords = (Tile.WIDTH / 2. - (label.get_rect().width / 2.), Tile.HEIGHT / 2. - (label.get_rect().height / 2.))
		self.image.blit(label,coords)
		self.rect = self.image.get_rect(center=self.pos)
		#self.value = 0
		#self.quantity = 0

	def setColor(self):
		if(self.squareType == "Normal"):
			return self.dic_colors['white']
		elif(self.squareType == "DL"):
			return self.dic_colors['blue'] 
		elif(self.squareType == "DP"):
			return self.dic_colors['orange']  
		elif(self.squareType == "TL"):
			return self.dic_colors['green']  
		elif(self.squareType == "TP"):
			 return self.dic_colors['red']  
		elif(self.squareType == "Start"):
			return self.dic_colors['black']   
		elif(self.squareType == "Letter"):
			return self.dic_colors['yellow']

	def setText(self):
		if(self.squareType == "Normal" or self.squareType == "Start" or self.squareType == "Letter"):
			return ""
		else:
			return self.squareType