
class Movie:
    """ Movie information including display attributes """
    
    def __init__(self,
                 title,
                 trailer_youtube_url=None,
                 poster_image_url=None,
                 run_time=None,
                 synopsis=None,
                 director=None):
        self.title = title
        self.trailer_youtube_url = trailer_youtube_url
        self.poster_image_url = poster_image_url
        self.run_time = run_time
        self.synopsis = synopsis
        self.director = director
