
class Movie:
    """ Class to save movie title and display attributes """
    def __init__(self, title=None, trailer_youtube_url=None, poster_image_url=None):
        self.title = title
        self.trailer_youtube_url = trailer_youtube_url
        self.poster_image_url = poster_image_url
