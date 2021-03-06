# Importing dependencies
import webbrowser


# This movie class contains information regarding the movie.
class Movie():
    """
    This is the movie class that takes in parameters including
    movie storyline, poster image, youtube trailer, main actor,
    and release date. Also has a function that opens web browser
    link.
    """

    # This assign the movie properties to self.
    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube, main_actor, release_date):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.main_actor = main_actor
        self.release_date = release_date

    # This instance method allows you to show the trailer when called.
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
