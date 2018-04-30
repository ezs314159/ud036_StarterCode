"""
Manage media displayed by the entertainment center website.
"""

class Movie:
    """ Manage information about a movie. """

    def __init__(self,
                 title,
                 trailer_youtube_url=None,
                 poster_image_url=None,
                 run_time=None,
                 synopsis=None,
                 director=None):
        """
        A data container for movie information.
        
        :param title"
            The title of the movie.
        :param trailer_youtube_url:
            A URL which will display a Youtube tailer video for the movie.
        :param poster_image_url:
            A URL for a poster image for the movie.
        :param run_time:
            Optional total run time of the movie in minutes.
        :param synopsis:
            Optional paragraph of text describing the movie.
        :param director:
            Optional name of the movie director, last name first.
        """
        self.title = title
        self.trailer_youtube_url = trailer_youtube_url
        self.poster_image_url = poster_image_url
        self.run_time = run_time
        self.synopsis = synopsis
        self.director = director
