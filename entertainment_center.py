import media
import fresh_tomatoes

Forrest_Gump = media.Movie('Forrest Gump', 
	'Life journey of a simple man Forrest Gump', 
	'https://images-na.ssl-images-amazon.com/images/M/MV5BYThjM2MwZGMtMzg3Ny00NGRkLWE4M2EtYTBiNWMzOTY0YTI4XkEyXkFqcGdeQXVyNDYyMDk5MTU@._V1_UY268_CR10,0,182,268_AL_.jpg',
	'https://www.youtube.com/watch?v=uPIEn0M8su0')

The_Notebook = media.Movie('The Notebook',
	'A love story of Allie and Noah',
	'http://nicholassparks.com/wp-content/uploads/2013/07/200406-the-notebook.jpeg',
	'https://www.youtube.com/watch?v=4M7LIcH8C9U')

Interstellar = media.Movie('Interstella',
	'Space exploration, humanity, and love',
	'https://upload.wikimedia.org/wikipedia/en/b/bc/Interstellar_film_poster.jpg',
	'https://www.youtube.com/watch?v=0vxOhd4qlnA')

Coherence = media.Movie('Coherence',
	'A night of supernatural occurrences',
	'https://images-na.ssl-images-amazon.com/images/M/MV5BNzQ3ODUzNDY2M15BMl5BanBnXkFtZTgwNzg0ODY2MTE@._V1_UX182_CR0,0,182,268_AL_.jpg',
	'https://www.youtube.com/watch?v=sEceDz1Rodc')

Catch_Me_If_You_Can = media.Movie('Catch Me If You Can',
	'''The story of Frank Abagnale committing fraud national-wide with a FBI agent pursueing after him''',
	'https://upload.wikimedia.org/wikipedia/en/4/4d/Catch_Me_If_You_Can_2002_movie.jpg',
	'https://www.youtube.com/watch?v=71rDQ7z4eFg')

Lock_Stock_And_Two_Smoking_Barrels = media.Movie('Lock, Stock and Two Smoking Barrels',
	'A botched card game triggers four friens, thugs, weed-growers, hard gangsters, loan sharks and debt collectors to collide with each other in a series of unexpected events',
	'https://images-na.ssl-images-amazon.com/images/M/MV5BMTAyN2JmZmEtNjAyMy00NzYwLThmY2MtYWQ3OGNhNjExMmM4XkEyXkFqcGdeQXVyNDk3NzU2MTQ@._V1_UX182_CR0,0,182,268_AL_.jpg',
	'https://www.youtube.com/watch?v=Y8MXn5No1Jc')

The_Avengers = media.Movie('The Avengers',
	'Superheroes protecting our planet',
	'https://i.annihil.us/u/prod/marvel/i/mg/6/50/521f70b81f7d3/portrait_incredible.jpg',
	'https://www.youtube.com/watch?v=eOrNdBpGMv8')

Mission_Impossible_4 = media.Movie('Mission: Impossible Ghost Protocol',
	'Ethan Hunt on his new mission to fight nuclear terrorism',
	'https://upload.wikimedia.org/wikipedia/en/b/b5/Mission_impossible_ghost_protocol.jpg',
	'https://www.youtube.com/watch?v=5NKFDP7uaLI')

Jurassic_World = media.Movie('Jurassic World',
	'New genetically modified hybrid dinosaur set loose in Jurassic Park',
	'http://cdn.playbuzz.com/cdn/fcbb825b-b56f-411a-9512-f9b70198c672/f478eb4c-210c-4656-90b6-ce640beff119.jpg',
	'https://www.youtube.com/watch?v=RFinNxS5KN4')


movies = [Forrest_Gump, The_Notebook, Interstellar, 
	Coherence, Catch_Me_If_You_Can, Lock_Stock_And_Two_Smoking_Barrels,
	The_Avengers, Mission_Impossible_4, Jurassic_World]

fresh_tomatoes.open_movies_page(movies)
