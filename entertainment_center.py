""" 
define favorite movies and display them in entertainment center
website.
"""

from media import Movie
from fresh_tomatoes import open_movies_page

# define information about all the movies for the entertainment center
movies = []
movies.append(Movie("Avatar",
              trailer_youtube_url="https://www.youtube.com/"
                    "watch?v=5PSNL1qE6VY",
              poster_image_url="https://s3.amazonaws.com/"
                    "ffe-ugc/intlportal2/dev-temp/en-US/"
                    "__5603af15335dd-4a38d2eebe46ae0c1e7104d341e9dde"
                    "f6b8c4794-00f8fcfabf9f0d18.jpg"))
movies.append(Movie("Arrival",
              trailer_youtube_url="https://www.youtube.com/"
                    "watch?v=tFMo3UJ4B4g",
              poster_image_url="https://ia.media-imdb.com/images/M/"
                    "MV5BMTExMzU0ODcxNDheQTJeQWpwZ15BbWU4MDE1OTI4MzAy."
                    "_V1_UX182_CR0,0,182,268_AL_.jpg"))
movies.append(Movie("Galaxy Quest",
              trailer_youtube_url="https://www.youtube.com/"
                    "watch?v=VtHM77IRkus",
              poster_image_url="http://img.moviepostershop.com/"
                    "galaxy-quest-movie-poster-1999-1020253192.jpg"))
movies.append(Movie("The Secret Life of Walter Mitty",
              trailer_youtube_url="https://www.youtube.com/"
                    "watch?v=HddkucqSzSM",
              poster_image_url="http://www.impawards.com/2013/posters/"
                    "secret_life_of_walter_mitty.jpg"))

# open a browser to display the entertainment center website
open_movies_page(movies)
