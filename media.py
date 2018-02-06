import webbrowser

class Movie():

    """This class provides a way to store movie related information"""

    VALID_RATINGS = ["G", "PG", "PG-13", "R", "NC-17"]

    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube, release_date, imdb_page):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.release_date = release_date
        self.imdb_page_url = imdb_page

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)

    def show_imdb_page(self):
        webbrowser.open(self.imdb_page_url)
