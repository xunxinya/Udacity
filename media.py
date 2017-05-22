import webbrowser

class Movie:
	'''The class stores movies with respective title, storyline, poster image and trailor link'''

	def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
		self.title = movie_title
		self.movie_storyline = movie_storyline
		self.poster_image_url = poster_image
		self.trailer_youtube_url = trailer_youtube

	#open the trailor on youtube in a webbrowser
	def show_trailer(self):
		webbrowser.open(self.trailer_youtube_url)
