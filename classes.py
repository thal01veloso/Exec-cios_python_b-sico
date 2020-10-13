class Guerreiro():
	def __init__(self):
		self.ataque = 300
		self.agilidade = 400
		self.defesa = 250
		self.magia = 0
	def add_ataque(self,n):
		print('{} de ataque foi adicionado ao seu guerreiro'.format(n))
		self.ataque = self.ataque + n
		return self.ataque
	def add_defesa(self,n):
		print('{} de ataque foi adicionado ao seu guerreiro'.format(n))
		self.defesa = self.defesa + n
		return self.defesa
goku = Guerreiro()
