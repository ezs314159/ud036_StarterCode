
from media import Movie
from fresh_tomatoes import open_movies_page

movies = []
movies.append(Movie(title="Avatar",
             trailer_youtube_url="tbd",
             poster_image_url="tbd"))
movies.append(Movie(title="Arrival",
             trailer_youtube_url="tbd",
             poster_image_url="tbd"))
movies.append(Movie(title="Galaxy Quest",
             trailer_youtube_url="tbd",
             poster_image_url="tbd"))

open_movies_page(movies)
