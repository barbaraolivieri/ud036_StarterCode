import webbrowser

class Movie():
	# Inicializando a classe com os atributos desejados
	def __init__(self,titulo,sinopse,poster,trailer):
		self.title = titulo
		self.storyline = sinopse
		self.poster_image_url = poster
		self.trailer_youtube_url = trailer
	# Método
	def mostrar_trailer(self):
		webbrowser.open(self.trailer)