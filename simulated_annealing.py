import numpy as np

class Dados:
	def __init__(self):
		self.coord = np.loadtxt('51.txt')
		self.matrix = np.zeros((51,51))
		aux = len(self.coord)
		
		dist = list()

		
		for i in self.coord:
			for j in self.coord:
				dist.append( ( (i[1]-j[1])**2 + (i[2]-j[2])**2)**0.5 )
		 
		for i in range(aux):
			for j in range(aux):
				self.matrix[i][j] = dist[j+(aux*i)]
		




if __name__ == "__main__":
	dados = Dados()
