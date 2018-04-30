"""
Manage media displayed by the entertainment center website.
"""

class Movie:
    """ 
    A data container for movie information.
    
    Attributes:
        title (str):  The title of the movie.
        trailer_youtube_url (str, optional): The URL of a Youtube
            tailer video for the movie.
        poster_image_url (str, optional):  The URL of a poster 
            image for the movie.
        run_time (int, optional):  Total run time of the movie
            in minutes.
        synopsis (str, optional): Brief text describing the movie.
        director (str, optional): Director name (last name first).
    """

    def __init__(self,
                 title,
                 trailer_youtube_url=None,
                 poster_image_url=None,
                 run_time=None,
                 synopsis=None,
                 director=None):
        """
        Return a new Movie object.
        
        The parameters are the movie title and optionally other 
        attributes of the class.
        """
        self.title = title
        self.trailer_youtube_url = trailer_youtube_url
        self.poster_image_url = poster_image_url
        self.run_time = run_time
        self.synopsis = synopsis
        self.director = director
