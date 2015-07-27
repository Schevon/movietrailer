import webbrowser


class Movie():
    # defining movie constructor and initializing its instance variables
    def __init__(self, title, poster_img, trailer_youtube_url, movie_desc):
        self.title = title
        self.poster_img = poster_img
        self.trailer_youtube_url = trailer_youtube_url
        self.movie_desc = movie_desc  
    
