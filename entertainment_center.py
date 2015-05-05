import media
import fresh_tomatoes

"""Create instances of each movie."""

toy_story = media.Movie("Toy Story",
			"A story of a boy and his toys that come to life.",
			"http://parkwaynews.net/corral/wp-content/uploads/2014/04/Toy-Story-Poster.jpg",
			"https://www.youtube.com/watch?v=vwyZH85NQC4",
    		"G")

avatar = media.Movie("Avatar",
			"A marine on an alien planet.",
			"http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg",
			"https://www.youtube.com/watch?v=5PSNL1qE6VY",
			"PG-13")

school_of_rock = media.Movie("School of Rock",
			"A wannabe rock star in need of cash poses as a substitute teacher at a prep school, and tries to turn his class into a rock band.",
			"http://ia.media-imdb.com/images/M/MV5BMjEwOTMzNjYzMl5BMl5BanBnXkFtZTcwNjczMTQyMQ@@._V1_SX214_AL_.jpg",
			"https://www.youtube.com/watch?v=3PsUJFEBC74",
			"PG-13")

ratatouille = media.Movie("Ratatouille",
			"A rat who can cook makes an unusual alliance with a young kitchen worker at a famous restaurant.",
			"http://a2.mzstatic.com/us/r30/Video/v4/a3/e8/c0/a3e8c0d9-f51d-24a5-f8b6-221452950cd4/RATATOUILLE_APPLE_US_E.jpg",
			"https://www.youtube.com/watch?v=c3sBBRxDAqk",
			"G")

casino_royale = media.Movie("Casino Royale",
			"Armed with a licence to kill, Secret Agent James Bond sets out on his first mission as 007 and must defeat a weapons dealer in a high stakes game of poker at Casino Royale, but things are not what they seem.",
			"http://www.movie-trivia-champs.com/wp-content/uploads/2013/12/casino-royale.jpg",
			"https://www.youtube.com/watch?v=36mnx8dBbGE",
			"PG-13")

the_interview = media.Movie("The Interview",
			"Dave Skylark and producer Aaron Rapoport run the celebrity tabloid show Skylark Tonight. When they land an interview with a surprise fan, North Korean dictator Kim Jong-un, they are recruited by the CIA to turn their trip to Pyongyang into an assassination mission.",
			"http://cdn.collider.com/wp-content/uploads/the-interview-poster1.jpg",
			"https://www.youtube.com/watch?v=frsvWVEHowg",
			"R")

super_troopers = media.Movie("Super Troopers",
			"Five Vermont state troopers, avid pranksters with a knack for screwing up, try to save their jobs and out-do the local police department by solving a crime.",
			"http://imgc.allpostersimages.com/images/P-488-488-90/40/4030/I2BLF00Z/posters/super-troopers-german-movie-poster-2001.jpg",
			"https://www.youtube.com/watch?v=6Wx5GgJhM9Y",
			"R")

"""Create an array of the instances.""" 
movies = [toy_story, avatar, school_of_rock, ratatouille, casino_royale, the_interview, super_troopers]

"""Feed array into open_movies_page from fresh tomatoes."""
fresh_tomatoes.open_movies_page(movies)